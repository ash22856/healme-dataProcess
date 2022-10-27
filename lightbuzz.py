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

def store_mocap_sitToStand(data,conn):
    cur = conn.cursor()
    subData = data['sitToStand']
    cur.execute('INSERT INTO mocap_sittostand VALUES (%s,%s,%s,%s,%s,%s,%s);',
    (subData['user_id'],subData['session_id'],subData['total_repetition'],subData['average_seated_knee_angle'],
    subData['rests'],subData['flagged_for_review'],subData['video']))

def store_mocap_shoulderROM(data,conn):
    cur = conn.cursor()
    subData = data['shoulderROM']
    cur.execute('INSERT INTO mocap_shoulderrom VALUES (%s,%s,%s,%s,%s);',
    (subData['user_id'],subData['session_id'],subData['shoulder_flexion'],
    subData['flagged_for_review'],subData['video']))

def store_mocap_SLB(data,conn):
    cur = conn.cursor()
    subData = data['SLB']
    cur.execute('INSERT INTO mocap_slb VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
    (subData['user_id'],subData['session_id'],subData['total_time_balanced'],
    subData['sway_in_hips'],subData['sway_in_shoulders'],subData['rotation_of_spine'],
    subData['lean'],subData['video']))

def store_mocap_gait(data,conn):
    cur = conn.cursor()
    subData = data['gait']
    cur.execute('INSERT INTO mocap_gait VALUES (%s,%s,%s,%s,%s,%s);',
    (subData['user_id'],subData['session_id'],subData['time'],
    subData['average'],subData['flagged_for_review'],subData['video']))

def store_mocap_step(data,conn):
    cur = conn.cursor()
    subData = data['step']
    cur.execute('INSERT INTO mocap_step VALUES (%s,%s,%s,%s,%s,%s);',
    (subData['user_id'],subData['session_id'],subData['repetitions'],
    subData['failed_repetitions'],subData['steps'],subData['rests']))

def store_mocap_TUG(data,conn):
    cur = conn.cursor()
    subData = data['TUG']
    cur.execute('INSERT INTO mocap_tug VALUES (%s,%s,%s,%s);',
    (subData['user_id'],subData['session_id'],
    subData['total_time'],subData['gait_used']))



    