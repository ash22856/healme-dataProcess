import pandas as pd
import json
import utils as uts
import random
import datetime


def store_general_foodrx(data,session_id,group_user_id,conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM foodrx_data WHERE session_id = %s AND group_user_id = %s;",(session_id,group_user_id))
    cur.execute("INSERT INTO foodrx_data VALUES (%s,%s,%s,%s,%s);",
    (session_id,data["endtime"],data["data_json_url"],data["starttime"],group_user_id))



def storeSummary(data,session_id,group_user_id,conn):
    sd = data['current']
    cur = conn.cursor()

    query = "INSERT INTO foodrx_summary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,sd["first_name"],sd["last_name"],sd["date_since"],sd["date_until"],
    sd["n_days_with_data"],sd["n_meals"],sd["n_meal_items"],sd["comparison_report_id"],sd["average_dash"],sd["morning_cals"],
    sd["lunchtime_cals"],sd["afternoon_cals"],sd["dinnertime_cals"],sd["evening_cals"],sd["morning_cals_sum"],sd["lunchtime_cals_sum"],
    sd["afternoon_cals_sum"],sd["dinnertime_cals_sum"],sd["evening_cals_sum"],sd["morning_carbs"],sd["lunchtime_carbs"],sd["afternoon_carbs"],
    sd["dinnertime_carbs"],sd["evening_carbs"],sd["morning_carbs_sum"],sd["lunchtime_carbs_sum"],sd["afternoon_carbs_sum"],
    sd["dinnertime_carbs_sum"],sd["evening_carbs_sum"],sd["feelings_statement"],sd["notes_statement"],sd["motivations_statement"],
    sd["diet_restrictions_statement"],group_user_id)
    cur.execute(query,params)


def store_rdi_response(data,session_id,group_user_id,conn):
    subData = data['current']["patient_rdi_response"]["nutrients"]
    cur = conn.cursor()

    for item in subData:
        query = "INSERT INTO foodrx_nutrients_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        params = (session_id,item["nutrient"],item["unit"],item["value_percent_of_target"],item["avg_daily_intake"],
        item["min_daily_intake"],item["max_daily_intake"],item["per_thousand_kcal"],item["target_value_low"],item["target_value_high"],group_user_id)

        cur.execute(query,params)


def store_rdi_images(data,session_id,group_user_id,conn):
    subData = data['current']['patient_rdi_images']
    cur = conn.cursor()

    for item in subData:
        query = "INSERT INTO foodrx_rdi_images VALUES (%s,%s,%s,%s,%s,%s);"
        params = (session_id,item["nutrient"],item["scoring_bucket"],item["image_name"],item["location"],group_user_id)

        cur.execute(query,params)


def store_avg_plate_resp(data,session_id,group_user_id,conn):
    cal_method = data['current']['average_plate_data_response']['calculation_method']
    subData = data['current']['average_plate_data_response']
    meal_list = ["breakfast","lunch","dinner","snack","overall"]
    cur = conn.cursor()

    for item in meal_list:
        query = "INSERT INTO foodrx_average_plate_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        params = (session_id,cal_method,item,subData[item]["protein"],subData[item]["fruit"],subData[item]["grains"],subData[item]["vegetable"],group_user_id)

        cur.execute(query,params)

    
def store_starPlot_resp(data,session_id,group_user_id,conn):
    subData = data['current']['patient_star_plot_response']
    cur = conn.cursor()

    query = "INSERT INTO foodrx_starplot VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,subData["patient_id"],subData["calorie_ratio"],subData["fat_ratio_pct_of_target"],subData["whole_grain_pct"],
    subData["fiber_pct_of_target"],subData["vegetable_pct_of_target"],subData["fruit_pct_of_target"],subData["non_red_meat_pct_of_protein"],subData["plant_based_pct"],
    subData["whole_foods_and_low_processed_foods"],subData["healthy_bev_pct_of_total"],subData["unhealthy_fat_kcal_pct_of_total"],subData["redmeat_frequency_weekly"],
    subData["poultry_frequency_weekly"],subData["ultraprocessed_pct_of_total"],group_user_id)

    cur.execute(query,params)


def store_beverage_freq_resp(data,session_id,group_user_id,conn):
    subData = data["current"]["beverage_frequency_response"]
    cur = conn.cursor()

    query = "INSERT INTO foodrx_beverage_freq_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,subData["milk_and_alternatives"],subData["sugary_beverage"],
    subData["alcohol"],subData["coffee_tea_cocoa"],subData["water"],subData["artificially_sweetened"],group_user_id)

    cur.execute(query,params)


def store_meal_resp(data,session_id,group_user_id,conn):
    subData = data['current']['food_dump_response']['rows']
    cur = conn.cursor()

    for item in subData:
        addon = " ".join(item["addons"])
        query = "INSERT INTO foodrx_meal_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (session_id,meal_date,meal_name,food_name,group_user_id) DO NOTHING;"
        params = (session_id,addon,item["carbohydrate_g"],
        item["food_name"],item["meal_date"],item["meal_name"],item["meal_note"],item["netcarb_g"],
        item["patient_note"],item["percent_eaten"],item["potassium_mg"],item["serving_unit_label"],
        item["servings"],item["type"],group_user_id)

        cur.execute(query,params)


def store_foodrx_images(data,session_id,group_user_id,conn):
    cur = conn.cursor()

    diet_score_image = data["current"]["diet_score_image"]
    macronutrient_distribution_image = data["current"]["macronutrient_distribution_image"]
    micronutrient_trends_image = data["current"]["micronutrient_trends_image"]
    average_plate_image = data["current"]["average_plate_image"]
    average_breakfast_plate_image = data["current"]["average_breakfast_plate_image"]
    average_lunch_plate_image = data["current"]["average_lunch_plate_image"]
    average_dinner_plate_image = data["current"]["average_dinner_plate_image"]
    average_breakfast_plate_serv_image = data["current"]["average_breakfast_plate_serv_image"]
    average_lunch_plate_serv_image = data["current"]["average_lunch_plate_serv_image"]
    average_dinner_plate_serv_image = data["current"]["average_dinner_plate_serv_image"]
    average_overall_plate_image = data["current"]["average_overall_plate_image"]
    glycemic_index_frequency_image = data["current"]["glycemic_index_frequency_image"]
    carb_daily_intake_image = data["current"]["carb_daily_intake_image"]
    sodium_dash_image = data["current"]["sodium_dash_image"]
    cholesterol_dash_image = data["current"]["cholesterol_dash_image"]
    saturated_fat_dash_image = data["current"]["saturated_fat_dash_image"]
    total_fat_dash_image = data["current"]["total_fat_dash_image"]
    protein_dash_image = data["current"]["protein_dash_image"]
    calcium_dash_image = data["current"]["calcium_dash_image"]
    magnesium_dash_image = data["current"]["magnesium_dash_image"]
    potassium_dash_image = data["current"]["potassium_dash_image"]
    fiber_dash_image = data["current"]["fiber_dash_image"]
    fat_frequency_image = data["current"]["fat_frequency_image"]
    water_frequency_image = data["current"]["water_frequency_image"]
    beverage_frequency_image = data["current"]["beverage_frequency_image"]
    plant_based_frequency_image = data["current"]["plant_based_frequency_image"]
    ultra_processed_frequency_image = data["current"]["ultra_processed_frequency_image"]
    grain_frequency_image = data["current"]["grain_frequency_image"]
    protein_frequency_image = data["current"]["protein_frequency_image"]
    star_plot_image = data["current"]["star_plot_image"]
    ghg_equivalent_kg_image = data["current"]["ghg_equivalent_kg_image"]

    query = "INSERT INTO foodrx_images VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,diet_score_image,macronutrient_distribution_image,micronutrient_trends_image,average_plate_image,average_breakfast_plate_image,
    average_lunch_plate_image,average_dinner_plate_image,average_breakfast_plate_serv_image,average_lunch_plate_serv_image,average_dinner_plate_serv_image,
    average_overall_plate_image,glycemic_index_frequency_image,carb_daily_intake_image,sodium_dash_image,cholesterol_dash_image,saturated_fat_dash_image,
    total_fat_dash_image,protein_dash_image,calcium_dash_image,magnesium_dash_image,potassium_dash_image,fiber_dash_image,fat_frequency_image,water_frequency_image,
    beverage_frequency_image,plant_based_frequency_image,ultra_processed_frequency_image,grain_frequency_image,protein_frequency_image,star_plot_image,ghg_equivalent_kg_image,group_user_id)

    cur.execute(query,params)
    

def store_foodrx_comments(data,session_id,group_user_id,conn):
    cur = conn.cursor()

    calories_by_period_comments = data["current"]["calories_by_period_comments"]
    carbs_by_period_comments = data["current"]["carbs_by_period_comments"]
    nutrients_summary_comments = data["current"]["nutrients_summary_comments"]
    glycemic_index_food_comments = data["current"]["glycemic_index_food_comments"]
    diet_score_comments = data["current"]["diet_score_comments"]
    macronutrient_distribution_comments = data["current"]["macronutrient_distribution_comments"]
    micronutrient_trends_comments = data["current"]["micronutrient_trends_comments"]
    average_plate_comments = data["current"]["average_plate_comments"]
    glycemic_index_frequency_comments = data["current"]["glycemic_index_frequency_comments"]
    carb_daily_intake_comments = data["current"]["carb_daily_intake_comments"]
    average_plant_protein_frequency_comments = data["current"]["average_plant_protein_frequency_comments"]
    average_fats_frequency_comments = data["current"]["average_fats_frequency_comments"]
    average_water_frequency_comments = data["current"]["average_water_frequency_comments"]
    average_grains_frequency_comments = data["current"]["average_grains_frequency_comments"]
    average_proteins_frequency_comments = data["current"]["average_proteins_frequency_comments"]

    query = "INSERT INTO foodrx_comments VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,calories_by_period_comments,carbs_by_period_comments,nutrients_summary_comments,glycemic_index_food_comments,diet_score_comments,
    macronutrient_distribution_comments,micronutrient_trends_comments,average_plate_comments,glycemic_index_frequency_comments,carb_daily_intake_comments,
    average_plant_protein_frequency_comments,average_fats_frequency_comments,average_water_frequency_comments,average_grains_frequency_comments,average_proteins_frequency_comments,group_user_id)

    cur.execute(query,params)


def store_foodrx_statements(data,session_id,group_user_id,conn):
    cur = conn.cursor()

    ghg_equivalent_kg_statements = data["current"]["ghg_equivalent_kg_statements"]
    calories_by_period_statements = data["current"]["calories_by_period_statements"]
    carbs_by_period_statements = data["current"]["carbs_by_period_statements"]
    macro_statements = data["current"]["macro_statements"]
    fruit_vegetable_statements = data["current"]["fruit_vegetable_statements"]
    fruit_vegetable_serv_statements = data["current"]["fruit_vegetable_serv_statements"]
    plant_based_frequency_statements = data["current"]["plant_based_frequency_statements"]
    ultra_processed_frequency_statements = data["current"]["ultra_processed_frequency_statements"]
    fat_frequency_statements = data["current"]["fat_frequency_statements"]
    omega_3_statement = data["current"]["omega_3_statement"]
    grain_frequency_statements = data["current"]["grain_frequency_statements"]
    fibre_statements = data["current"]["fibre_statements"]
    protein_frequency_statements = data["current"]["protein_frequency_statements"]
    fruit_frequency_statements = data["current"]["fruit_frequency_statements"]
    vegetable_frequency_statements = data["current"]["vegetable_frequency_statements"]
    gi_frequency_statements = data["current"]["gi_frequency_statements"]
    sodium_dash_statements = data["current"]["sodium_dash_statements"]
    cholesterol_dash_statements = data["current"]["cholesterol_dash_statements"]
    saturated_fat_dash_statements = data["current"]["saturated_fat_dash_statements"]
    total_fat_dash_statements = data["current"]["total_fat_dash_statements"]
    protein_dash_statements = data["current"]["protein_dash_statements"]
    calcium_dash_statements = data["current"]["calcium_dash_statements"]
    magnesium_dash_statements = data["current"]["magnesium_dash_statements"]
    potassium_dash_statements = data["current"]["potassium_dash_statements"]
    fiber_dash_statements = data["current"]["fiber_dash_statements"]

    query = "INSERT INTO foodrx_statements VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,ghg_equivalent_kg_statements,calories_by_period_statements,carbs_by_period_statements,
    macro_statements,fruit_vegetable_statements,fruit_vegetable_serv_statements,plant_based_frequency_statements,ultra_processed_frequency_statements,
    fat_frequency_statements,omega_3_statement,grain_frequency_statements,fibre_statements,protein_frequency_statements,fruit_frequency_statements,
    vegetable_frequency_statements,gi_frequency_statements,sodium_dash_statements,cholesterol_dash_statements,saturated_fat_dash_statements,
    total_fat_dash_statements,protein_dash_statements,calcium_dash_statements,magnesium_dash_statements,potassium_dash_statements,fiber_dash_statements,group_user_id)

    cur.execute(query,params)


def store_foodrx_goals(data,session_id,group_user_id,conn):
    subData = data['current']['goals']
    cur = conn.cursor()

    for item in subData:
        query = "INSERT INTO foodrx_goals VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        params = (session_id,item["patient_id"],item["goal_id"],item["goal_type"],item["change"],item["target_name"],
        item["target_display_name"],item["target_unit"],item["target_value"],item["period"],item["start_date"],item["end_date"],
        item["range_value"],item["range_success_count"],item["range_total_count"],item["missed_logging_opportunities"],item["statement"],group_user_id)

        cur.execute(query,params)


def store_summ_statement(data,session_id,group_user_id,conn):
    subData = data["current"]["summary_statement"]
    date_since = subData['date_since']
    date_until = subData['date_until']
    cur = conn.cursor()

    for item in subData['results']:
        query = "INSERT INTO foodrx_summary_statement VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        params = (session_id,date_since,date_until,item["id"],item["category"],
        item["sub_category"],item["type"],item["text"],group_user_id)

        cur.execute(query,params)


def store_clin_summ_statement(data,session_id,group_user_id,conn):
    subData = data["current"]["clinical_summary_statement"]
    date_since = subData['date_since']
    date_until = subData['date_until']
    cur = conn.cursor()

    for item in subData['results']:
        query = "INSERT INTO foodrx_clinical_summary_statement VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        params = (session_id,date_since,date_until,item["id"],item["category"],
        item["sub_category"],item["type"],item["text"],group_user_id)

        cur.execute(query,params)


def dateFormat(date):
    m_dic = {
        'January': "01",
        'February': "02",
        'March': "03",
        'April': "04",
        'May': "05",
        'June': "06",
        'July': "07",
        'August': "08",
        'September': "09",
        'October': "10",
        'November': "11",
        'December': "12"
        }
    
    [md,year] = date.split(",")
    [day,month] = md.split(" ")
    
    if int(day) < 10 :
        day = "0"+day
    new_date = year+"-"+m_dic[month]+day

    return new_date

def store_rand_summ(data,session_id,creater,curr_date,modifier,modi_date,conn):
    selected_dates = select_random_dates(data)
    
    date_day_dic = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"
    }

    resp = []
    days_str = ""
    for v in selected_dates.values():
        days_str += date_day_dic[v]
        days_str += " "
    
    days_str += "meals updated to the database for patient "+str(session_id)
    cur = conn.cursor()
    subData = data["current"]['food_dump_response']['rows']
    
    for item in subData:
        if item["meal_date"] in selected_dates:
            addon = " ".join(item["addons"])
            query = "INSERT INTO foodrx_meal_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (session_id,meal_date,meal_name,food_name) DO NOTHING;"
            params = (session_id,creater,curr_date,modifier,modi_date,addon,item["carbohydrate_g"],
            item["food_name"],item["meal_date"],item["meal_name"],item["meal_note"],item["netcarb_g"],
            item["patient_note"],item["percent_eaten"],item["potassium_mg"],item["serving_unit_label"],
            item["servings"],item["type"])

            cur.execute(query,params)

            resp.append(item)

    return (days_str,resp)

def store_summ_byDate(data,date,session_id,conn):
    cur = conn.cursor()
    resp = []
    info_str = ""
    subData = data["current"]['food_dump_response']['rows']

    for item in subData:
        if item["meal_date"] == date:
            addon = " ".join(item["addons"])
            query = "INSERT INTO foodrx_meal_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (session_id,meal_date,meal_name,food_name) DO NOTHING;"
            params = (session_id,addon,item["carbohydrate_g"],
            item["food_name"],item["meal_date"],item["meal_name"],item["meal_note"],item["netcarb_g"],
            item["patient_note"],item["percent_eaten"],item["potassium_mg"],item["serving_unit_label"],
            item["servings"],item["type"])

            cur.execute(query,params)
            resp.append(item)
    
    if resp == []:
        info_str = "Please enter a valid date in yyyy-mm-dd format"
    else:
        info_str = "Meal data on "+date+" has been updated for patient "+str(session_id)
    return (info_str,resp)


def store_gi_resp(data,session_id,group_user_id,conn):
    cur = conn.cursor()
    
    breakfast = data["current"]["glycemic_index_frequency_response"]["breakfast"]
    lunch = data["current"]["glycemic_index_frequency_response"]["lunch"]
    dinner = data["current"]["glycemic_index_frequency_response"]["dinner"]
    snack = data["current"]["glycemic_index_frequency_response"]["snack"]

    meal_lst = [breakfast,lunch,dinner,snack]
    total_high_freq = 0
    total_low_freq = 0
    total_medium_freq = 0
    for item in meal_lst:
        if "high" not in item.keys():
            item["high"] = 0
        if "low" not in item.keys():
            item["low"] = 0
        if "medium" not in item.keys():
            item["medium"] = 0

        total_high_freq += item["high"]
        total_low_freq += item["low"]
        total_medium_freq += item["medium"]    
    
    low_gi_foods = data["current"]["low_gi1"]+", "+data["current"]["low_gi2"]+", "+data["current"]["low_gi3"]+", "+data["current"]["low_gi4"]+", "+data["current"]["low_gi5"]
    high_gi_foods = data["current"]["high_gi1"]+", "+data["current"]["high_gi2"]+", "+data["current"]["high_gi3"]+", "+data["current"]["high_gi4"]+", "+data["current"]["high_gi5"]
    
    delete_query = "DELETE FROM foodrx_gi_resp WHERE session_id = %s;"

    cur.execute(delete_query,(session_id,))

    update_query = "INSERT INTO foodrx_gi_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    update_params = (session_id,high_gi_foods,low_gi_foods,breakfast["high"],breakfast["low"],
    breakfast["medium"],lunch["high"],lunch["low"],lunch["medium"],dinner["high"],dinner["low"],dinner["medium"],snack["high"],
    snack["low"],snack["medium"],total_high_freq,total_low_freq,total_medium_freq,group_user_id)

    cur.execute(update_query,update_params)

    
def store_macro_value(data,session_id,group_user_id,conn):
    cur = conn.cursor()

    subData = data["current"]["macro_value"]
    query = "INSERT INTO foodrx_macro_pct_resp VALUES (%s,%s,%s,%s,%s,%s);"
    params = (session_id,subData["Unsaturated Fat"],subData["Saturated Fat"],subData["Carbohydrates"],subData["Protein"],group_user_id)
    cur.execute(query,params)


def store_macro_freq(data,session_id,group_user_id,conn):
    cur = conn.cursor()

    healthy_fat = data["current"]["fat_frequency_value"]["Healthy Fats"]
    unhealthy_fat = data["current"]["fat_frequency_value"]["Unhealthy Fats"]
    whole_grain = data["current"]["grain_frequency_value"]["Whole Grain"]
    refine_grain = data["current"]["grain_frequency_value"]["Refined Grain"]
    plant_based = data["current"]["plant_based_frequency_value"]["Plant-based"]
    non_plant_based = data["current"]["plant_based_frequency_value"]["Not Plant-based"]
    less_processed = data["current"]["ultra_processed_frequency_value"]["Whole and less processed foods"]
    ultra_processed = data["current"]["ultra_processed_frequency_value"]["Ultra-processed"]
    red_meat = data["current"]["protein_frequency_value"]["Red Meat"]
    poultry = data["current"]["protein_frequency_value"]["Poultry"]
    seafood = data["current"]["protein_frequency_value"]["Seafood"]
    plant_protein = data["current"]["protein_frequency_value"]["Plant Protein"]
    diary_egg = data["current"]["protein_frequency_value"]["Dairy & Egg"]

    query = "INSERT INTO foodrx_macro_freq_resp VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    params = (session_id,healthy_fat,unhealthy_fat,whole_grain,refine_grain,plant_based,non_plant_based,
    less_processed,ultra_processed,red_meat,poultry,seafood,plant_protein,diary_egg,group_user_id)

    cur.execute(query,params)

def store_meal_counts(data,session_id,group_user_id,conn):
    cur = conn.cursor()
    breakfast_count = data['current']['meal_frequency_response']['meals_per_day']['breakfast']
    lunch_count = data['current']['meal_frequency_response']['meals_per_day']['lunch']
    dinner_count = data['current']['meal_frequency_response']['meals_per_day']['dinner']
    snack_count = data['current']['meal_frequency_response']['meals_per_day']['snack']

    query = "INSERT INTO foodrx_meals_count VALUES (%s,%s,%s,%s,%s,%s);"
    params = (session_id,breakfast_count,lunch_count,dinner_count,snack_count,group_user_id)
    cur.execute(query,params)



def select_random_dates(data):
    date_since = data["current"]["date_since"]
    date_until = data["current"]["date_until"]
    date_range = pd.date_range(start=date_since,end=date_until).to_series()
    bdate_range = pd.bdate_range(start=date_since,end=date_until).to_series()
    bdate_count = len(bdate_range)
    

    dates = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
    for d in date_range:
        dates[d.dayofweek].append(d)

    selected_dates = {}
    if bdate_count < 2:
        selected_dates[dates[0]] = dates[0].dayofweek
    else:
        wds_count = 0
        while wds_count < 2:
            rand = random.randint(0,4)
            if dates[rand]==[]:
                continue
            item = dates[rand].pop()
            selected_dates[str(item).split()[0]] = item.dayofweek
            wds_count += 1
    
    rand_we = random.randint(5,6)
    if dates[rand_we]!=[]:
        item = dates[rand_we].pop()
        selected_dates[str(item).split()[0]] = item.dayofweek 
    else:
        if rand_we == 5:
            if dates[6]!=[]:
                item = dates[6].pop()
                selected_dates[str(item).split()[0]] = item.dayofweek
        else:
            if dates[5]!=[]:
                item = dates[5].pop()
                selected_dates[str(item).split()[0]] = item.dayofweek
    
    return selected_dates
    

def get_random_date_meals(data):
    rand_dates = select_random_dates(data)
    
    subData = data["current"]['food_dump_response']['rows']
    results = {}

    date_day_dic = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"
    }

    for item in subData:
        if item["meal_date"] in rand_dates.keys():
            new_key = item["meal_date"] + ", " +date_day_dic[rand_dates[item["meal_date"]]]
            if new_key not in results.keys():
                results[new_key] = []
            results[new_key].append(item)
    
    return results


def get_random_dates_total_nutrient(data,nutrient):
    rand_meals = get_random_date_meals(data)
    total = {}

    if nutrient == "carb":
        nutrient = "carbohydrate_g"
    elif nutrient == "netcarb":
        nutrient = "netcarb_g"
    elif nutrient == "potassium":
        nutrient = "potassium_mg"
    for k in rand_meals.keys():
        total[k] = 0
        for item in rand_meals[k]:
            total[k] += item[nutrient]
    
    return total

