import pandas as pd
import utils as uts

def store_general_lightbuzz(data,user_id,creater,curr_date,modifier,modi_date,conn):
    cur = conn.cursor()

    cur.execute("DELETE FROM mocap WHERE mocap_id = %s;",(user_id,))
    cur.execute("DELETE FROM light_buzz WHERE light_buzz_id = %s;",(user_id,))
    cur.execute("INSERT INTO light_buzz VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
    (user_id,creater,curr_date,modifier,modi_date,data["endtime"],data["data_csv_url"],data["starttime"],
    data["data_video_url"],data["assessment_type"],data["group_user_id"]))


def store_lightbuzz_movements(data,user_id,conn):
    cur = conn.cursor()

    for (idx,row) in data.iterrows():
        cur.execute("DELETE FROM mocap WHERE timestamp = %s AND mocap_id = %s;",(str(row.loc["Timestamp"]),user_id))
        cur.execute("INSERT INTO mocap VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *;", 
        (user_id,str(row.loc["Timestamp"]),row.loc["Left elbow angle"],row.loc["Right elbow angle"],row.loc["Left knee angle"],
        row.loc["Right knee angle"],row.loc["Nose(X)"],row.loc["Nose(Y)"],row.loc["Neck(X)"],row.loc["Neck(Y)"],row.loc["ShoulderRight(X)"],
        row.loc["ShoulderRight(Y)"],row.loc["ElbowRight(X)"],row.loc["ElbowRight(Y)"],
        row.loc["WristRight(X)"],row.loc["WristRight(Y)"],row.loc["ShoulderLeft(X)"],row.loc["ShoulderLeft(Y)"],row.loc["ElbowLeft(X)"],
        row.loc["ElbowLeft(Y)"],row.loc["WristLeft(X)"],row.loc["WristLeft(Y)"],row.loc["HipRight(X)"],row.loc["HipRight(Y)"],row.loc["KneeRight(X)"],row.loc["KneeRight(Y)"],
        row.loc["AnkleRight(X)"],row.loc["AnkleRight(Y)"],row.loc["HipLeft(X)"],row.loc["HipLeft(Y)"],row.loc["KneeLeft(X)"],row.loc["KneeLeft(Y)"],
        row.loc["AnkleLeft(X)"],row.loc["AnkleLeft(Y)"],row.loc["EyeRight(X)"],row.loc["EyeRight(Y)"],row.loc["EyeLeft(X)"],row.loc["EyeLeft(Y)"],
        row.loc["EarRight(X)"],row.loc["EarRight(Y)"],row.loc["EarLeft(X)"],row.loc["EarLeft(Y)"],row.loc["FootLeft(X)"],row.loc["FootLeft(Y)"],
        row.loc["FootRight(X)"],row.loc["FootRight(Y)"],row.loc["Pelvis(X)"],row.loc["Pelvis(Y)"],row.loc["Waist(X)"],row.loc["Waist(Y)"],
        row.loc["Chest(X)"],row.loc["Chest(Y)"],user_id))

    