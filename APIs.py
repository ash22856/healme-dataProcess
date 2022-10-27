from ast import Dict
import json
from fastapi import FastAPI,Response,status,HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import BIGINT
import utils as uts
import boto3
import foodrx as frx
import lightbuzz as lbz
import survey as sv
import garmin as gm


app = FastAPI()

'''
Params needed: 
patient ID: int, 
data type: str
actual data: json
'''

class Mocap_Post(BaseModel):
    time_stamp : str = Field(...,alias="Timestamp")
    left_elbow_angle : str = Field(...,alias="Left elbow angle")
    right_elbow_angle : str = Field(...,alias="Right elbow angle")
    left_knee_angle : str = Field(...,alias="Left knee angle")
    right_knee_angle : str = Field(...,alias="Right knee angle") 
    nose_x : str = Field(...,alias="Nose(X)")
    nose_y : str = Field(...,alias="Nose(Y)")
    neck_x : str = Field(...,alias="Neck(X)")
    neck_y : str = Field(...,alias="Neck(Y)")
    shoulderRight_x : str = Field(...,alias="ShoulderRight(X)")
    shoulderRight_y : str = Field(...,alias="ShoulderRight(Y)")
    elbowRight_x : str = Field(...,alias="ElbowRight(X)")
    elbowRight_y : str = Field(...,alias="ElbowRight(Y)")
    wristRight_x : str = Field(...,alias="WristRight(X)")
    wristRight_y : str = Field(...,alias="WristRight(Y)")
    shoulderLeft_x : str = Field(...,alias="ShoulderLeft(X)")
    shoulderLeft_y : str = Field(...,alias="ShoulderLeft(Y)")
    elbowLeft_x : str = Field(...,alias="ElbowLeft(X)")
    elbowLeft_y : str = Field(...,alias="ElbowLeft(Y)")
    wristLeft_x : str = Field(...,alias="WristLeft(X)")
    wristLeft_y : str = Field(...,alias="WristLeft(Y)")
    hipRight_x : str = Field(...,alias="HipRight(X)")
    hipRight_y : str = Field(...,alias="HipRight(Y)")
    kneeRight_x : str = Field(...,alias="KneeRight(X)")
    kneeRight_y : str = Field(...,alias="KneeRight(Y)")
    ankleRight_x : str = Field(...,alias="AnkleRight(X)")
    ankleRight_y : str = Field(...,alias="AnkleRight(Y)")
    hipLeft_x : str = Field(...,alias="HipLeft(X)")
    hipLeft_y : str = Field(...,alias="HipLeft(Y)")
    kneeLeft_x : str = Field(...,alias="KneeLeft(X)")
    kneeLeft_y : str = Field(...,alias="KneeLeft(Y)")
    ankleLeft_x : str = Field(...,alias="AnkleLeft(X)")
    ankleLeft_y : str = Field(...,alias="AnkleLeft(Y)")
    eyeRight_x : str = Field(...,alias="EyeRight(X)")
    eyeRight_y : str = Field(...,alias="EyeRight(Y)")
    eyeLeft_x : str = Field(...,alias="EyeLeft(X)")
    eyeLeft_y : str = Field(...,alias="EyeLeft(Y)")
    earRight_x : str = Field(...,alias="EarRight(X)")
    earRight_y : str = Field(...,alias="EarRight(Y)")
    earLeft_x : str = Field(...,alias="EarLeft(X)")
    earLeft_y : str = Field(...,alias="EarLeft(Y)")
    footLeft_x : str = Field(...,alias="FootLeft(X)")
    footLeft_y : str = Field(...,alias="FootLeft(Y)")
    footRight_x : str = Field(...,alias="FootRight(X)")
    footRight_y : str = Field(...,alias="FootRight(Y)")
    pelvis_x : str = Field(...,alias="Pelvis(X)")
    pelvis_y: str = Field(...,alias="Pelvis(Y)")
    waist_x : str = Field(...,alias="Waist(X)")
    waist_y : str = Field(...,alias="Waist(Y)")
    chest_x : str = Field(...,alias="Chest(X)")
    chest_y : str = Field(...,alias="Chest(Y)")



try:
    conn = uts.connect(host_name='localhost',database_name='intern',user_name='postgres',password='zs1178771178')
    print("Database connection successful")
    cred = ""
except Exception as error:
    print("Database connection failed")
    print("Error: ",error)


    
@app.get("/MocapData")
async def get_data(patient_id:int):
    cur = conn.cursor()
    cur.execute("Select * from mocap WHERE patient_id = %s;",(patient_id,))
    data = cur.fetchall()
    conn.commit()
    return {"current_data":data}


@app.delete("/MocapData")
async def delete_mocap_data(patient_id:int):
    cur = conn.cursor()
    cur.execute("DELETE FROM mocap where patient_id = %s;",(patient_id,))
    conn.commit()
    return {"Message":"Data deleted"}

@app.post("/updateUserLightbuzz")
async def updateData(id:int):
    id = str(id)
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    key = "light_buzz" + "/user" + id + ".json"
    response = s3.Object(bucket_name,key)
    obj = response.get()['Body'].read().decode('utf-8')
    obj = json.loads(obj)

    user_id = id
    creater = obj["created_by"]
    created_date = obj["created_date"]
    modifier = obj["last_modified_by"]
    modi_date = obj["last_modified_date"]

    csv_data = uts.readCSV(obj["data_csv_url"]).astype("int")
    csv_data = csv_data.astype({'Timestamp':'str'})
        
    lbz.store_general_lightbuzz(obj,user_id,creater,created_date,modifier,modi_date,conn)
    lbz.store_lightbuzz_movements(csv_data,user_id,conn)

    conn.commit()
    return {"Message": "Lightbuzz data updated for user" + str(id)}
    

@app.post("/updateUserFoodRX")
async def updateData(session_id:int,group_user_id:int):
    cur = conn.cursor()

    session_id = str(session_id)
    group_user_id = str(group_user_id)
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    key = "foodrx" + "/user" + session_id + ".json"
    response = s3.Object(bucket_name,key)
    obj = response.get()['Body'].read().decode('utf-8')
    obj = json.loads(obj)

    
    creater = obj["created_by"]
    created_date = obj["created_date"]
    modifier = obj["last_modified_by"]
    modi_date = obj["last_modified_date"]

    if session_id == '1':
        json_data = uts.readJSON("foodrx.json")
    elif session_id == '2':
        json_data = uts.readJSON("foodrx2.json")

    # frx.store_general_foodrx(obj,session_id,group_user_id,conn)
    # frx.storeSummary(json_data,session_id,group_user_id,conn)
    # frx.store_rdi_response(json_data,session_id,group_user_id,conn)
    # frx.store_rdi_images(json_data,session_id,group_user_id,conn)
    # frx.store_avg_plate_resp(json_data,session_id,group_user_id,conn)
    # frx.store_starPlot_resp(json_data,session_id,group_user_id,conn)
    # frx.store_beverage_freq_resp(json_data,session_id,group_user_id,conn)
    # frx.store_meal_resp(json_data,session_id,group_user_id,conn)
    # frx.store_foodrx_images(json_data,session_id,group_user_id,conn)
    # frx.store_foodrx_comments(json_data,session_id,group_user_id,conn)
    # frx.store_foodrx_statements(json_data,session_id,group_user_id,conn)
    # frx.store_foodrx_goals(json_data,session_id,group_user_id,conn)
    # frx.store_summ_statement(json_data,session_id,group_user_id,conn)
    # frx.store_clin_summ_statement(json_data,session_id,group_user_id,conn)
    # frx.store_gi_resp(json_data,session_id,group_user_id,conn)
    # frx.store_macro_value(json_data,session_id,group_user_id,conn)
    # frx.store_macro_freq(json_data,session_id,group_user_id,conn)
    frx.store_meal_counts(json_data,session_id,group_user_id,conn)

    conn.commit()
    return {"Message": " FoodRX data updated for user with group_user_id "+str(group_user_id)}


@app.post("/updateUserGarmin")
async def updateGarmin(credentials:str):
    cur = conn.cursor()
    
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    healthKey = "garmin/" +credentials + "/" + credentials + "_healthSummary.json"
    activityKey = "garmin/" +credentials + "/" + credentials + "_activitySummary.json"
    sleepKey = "garmin/" + credentials +'/' +credentials + "_sleepSummary.json"
    generalKey = "garmin/" +credentials + "/" + credentials + ".json"
    hrvKey = "garmin/" +credentials + "/" + credentials + "_hrvSummary.json"

    generalResponse = s3.Object(bucket_name,generalKey)
    healthResponse = s3.Object(bucket_name,healthKey)
    activityResponse = s3.Object(bucket_name,activityKey)
    sleepResponse = s3.Object(bucket_name,sleepKey)
    hrvResponse = s3.Object(bucket_name,hrvKey)

    generalObj = generalResponse.get()['Body'].read().decode('utf-8')
    healthObj = healthResponse.get()['Body'].read().decode('utf-8')
    activityObj = activityResponse.get()['Body'].read().decode('utf-8')
    sleepObj = sleepResponse.get()['Body'].read().decode('utf-8')
    hrvObj = hrvResponse.get()['Body'].read().decode('utf-8')
    
    generalObj = json.loads(generalObj)
    healthObj = json.loads(healthObj)['healthSummary']
    activityObj = json.loads(activityObj)['ActivitySummary']
    sleepObj = json.loads(sleepObj)['sleepSummary']
    hrvObj = json.loads(hrvObj)['hrvSummary']

    # gm.store_general_garmin(generalObj,conn)
    gm.store_health_summary(healthObj,conn)
    # gm.store_activity_summary(activityObj,conn)
    # gm.store_hrv_summary(hrvObj,conn)
    # gm.store_sleep_summary(sleepObj,conn)
    

    conn.commit()
    return {"Message":"Garmin data stored for user with credentials "+ credentials}

@app.post("/updateUserMocapSummary")
async def updateMocap(user_id:int, session_id:int):
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    key = "light_buzz/" + str(user_id) + '/session' + str(session_id) + '.json'
    response = s3.Object(bucket_name,key)
    obj = response.get()['Body'].read().decode('utf-8')
    obj = json.loads(obj)

    lbz.store_mocap_sitToStand(obj,conn)
    lbz.store_mocap_shoulderROM(obj,conn)
    lbz.store_mocap_SLB(obj,conn)
    lbz.store_mocap_gait(obj,conn)
    lbz.store_mocap_step(obj,conn)
    lbz.store_mocap_TUG(obj,conn)

    conn.commit()
    return {"Message": "MoCap data of session " + str(session_id) + " stored for user with user_id " + str(user_id)}


@app.post("/randomMealSummary")
async def store_random_meal_summary(id:int):
    id = str(id)
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    key = "foodrx" + "/user" + id + ".json"
    response = s3.Object(bucket_name,key)
    obj = response.get()['Body'].read().decode('utf-8')
    obj = json.loads(obj)

    user_id = id
    creater = obj["created_by"]
    created_date = obj["created_date"]
    modifier = obj["last_modified_by"]
    modi_date = obj["last_modified_date"]

    json_data = uts.readJSON("foodrx.json")

    (info_str,resp_data) = frx.store_rand_summ(json_data,user_id,creater,created_date,modifier,modi_date,conn)
    conn.commit()

    return {info_str : resp_data}


@app.post("/mealSummaryByDate")
async def store_meal_summary_by_date(id:int,date:str):
    id = str(id)
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    key = "foodrx" + "/user" + id + ".json"
    response = s3.Object(bucket_name,key)
    obj = response.get()['Body'].read().decode('utf-8')
    obj = json.loads(obj)

    user_id = id
    creater = obj["created_by"]
    created_date = obj["created_date"]
    modifier = obj["last_modified_by"]
    modi_date = obj["last_modified_date"]

    json_data = uts.readJSON("foodrx.json")

    (info_str,resp_data) = frx.store_summ_byDate(json_data,date,user_id,creater,created_date,modifier,modi_date,conn)
    conn.commit()

    return {info_str : resp_data}

@app.post("updateSurvey")
async def store_survey_data(table:str):
    cur = conn.cursor()
    
    s3 = boto3.resource("s3")
    bucket_name = "acc-test-bucket-1"
    key = table + ".json"
    response = s3.Object(bucket_name,key)
    obj = response.get()['Body'].read().decode('utf-8')
    obj = json.loads(obj)

    created_by = obj["created_by"]
    created_date = obj["created_date"]
    modified_by = obj["last_modified_by"]
    modified_date = obj["last_modified_date"]

    csv_data = uts.readCSV(obj["data_csv_url"]).astype("int")
    
    if table == "eq5dl":
        sv.store_survey_eq5dl(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "sf36":
        sv.store_survey_sf36(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "gad7_anxiety":
        sv.store_survey_gad7_anxiety(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "cdrisc_10":
        sv.store_survey_cdrisc_10(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "djg":
        sv.store_survey_djg(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "who":
        sv.store_survey_who(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "lefs":
        sv.store_survey_lefs(csv_data,conn,created_by,created_date,modified_by,modified_date)
    elif table == "uefs":
        sv.store_survey_uefs(csv_data,conn,created_by,created_date,modified_by,modified_date)
    
    conn.commit()

    return {"Message":table + "data updated"}

    