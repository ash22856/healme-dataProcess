def store_survey_eq5dl(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_eq5dl e WHERE e.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_eq5dl VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["eq_5d_m"],item["eq_5d_sc"],
        item["eq_5d_ua"],item["eq_5d_pain"],item["eq_5d_anx"],item["eq_5d_anx"]))

def store_survey_cdrisc_10(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_cdrisc_10 c WHERE c.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_cdrisc_10 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["Biological Sex"],item["Group #"],
        item["Data Access"],item["risc_1"],item["risc_2"],item["risc_3"],item["risc_4"],item["risc_5"].item["risc_6"],item["risc_7"],
        item["risc_8"],item["risc_9"],item["risc_10"],item["Score out of 40"]))


def store_survey_djg(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_djg d WHERE d.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_djg VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["dejong_1"],item["dejong_2"],
        item["dejong_3"],item["dejong_4"],item["dejong_5"],item["dejong_6"],item["Score out of 6"]))



def store_survey_gad7_anxiety(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_gad7_anxiety g WHERE g.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_gad7_anxiety VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["gad_1"],item["gad_2"],
        item["gad_3"],item["gad_4"],item["gad_5"],item["gad_6"],item["gad_7"],item["Score out of 21"]))


def store_survey_lefs(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_lefs l WHERE l.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_lefs VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["lefs_1"],item["lefs_2"],
        item["lefs_3"],item["lefs_4"],item["lefs_5"],item["lefs_6"],item["lefs_7"],item["lefs_8"],item["lefs_9"],item["lefs_10"],
        item["lefs_11"],item["lefs_12"],item["lefs_13"],item["lefs_14"],item["lefs_15"],item["lefs_16"],item["lefs_17"],item["lefs_18"],
        item["lefs_19"],item["lefs_20"],item["Score out of 80"]))


def store_survey_sf36(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_sf36 s WHERE s.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_sf36 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["sf36_1"],item["sf36_2"],
        item["sf36_3"],item["sf36_4"],item["sf36_5"],item["sf36_6"],item["sf36_7"],item["sf36_8"],item["sf36_9"],item["sf36_10"],
        item["sf36_11"],item["sf36_12"],item["sf36_13"],item["sf36_14"],item["sf36_15"],item["sf36_16"],item["sf36_17"],item["sf36_18"],
        item["sf36_19"],item["sf36_20"],item["sf36_21"],item["sf36_22"],item["sf36_23"],item["sf36_24"],item["sf36_25"],item["sf36_26"],
        item["sf36_27"],item["sf36_28"],item["sf36_29"],item["sf36_30"],
        item["sf36_31"],item["sf36_32"],item["sf36_33"],item["sf36_34"],item["sf36_35"],item["sf36_36"],item["Physical Functioning"],
        item["Role limitations due to physical health"],item["Role limitations due to emotional problems"],
        item["Energy/fatigue"],item["Emotional well-being"],item["Social functioning"],item["Pain"],item["General health"]))


def store_survey_uefs(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]

        delete_query = "DELETE FROM survey_uefs u WHERE u.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_uefs VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["uefs_1"],item["uefs_2"],
        item["uefs_3"],item["uefs_4"],item["uefs_5"],item["uefs_6"],item["uefs_7"],item["uefs_8"],item["uefs_9"],item["uefs_10"],
        item["uefs_11"],item["uefs_12"],item["uefs_13"],item["uefs_14"],item["uefs_15"],item["uefs_16"],item["uefs_17"],item["uefs_18"],
        item["uefs_19"],item["uefs_20"],item["Score out of 80"]))


def store_survey_who(data,conn,created_by,created_date,last_modi_by,last_modi_date):
    cur = conn.cursor()

    for item in data:
        study_id = item["study_id"]
    
        delete_query = "DELETE FROM survey_who w WHERE w.study_id = %s;"
        cur.execute(delete_query,(study_id,))
        update_query = "INSERT INTO survey_who VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(update_query,(study_id,created_by,created_date,last_modi_by,last_modi_date,item["who5_1"],item["who5_2"],
        item["who5_3"],item["who5_4"],item["who5_5"],item["sum"],item["Score out of 100"]))