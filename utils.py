from email import header
import pandas as pd
import requests
import json
from operator import index
import psycopg2
from sqlalchemy import create_engine

# read files into the csv format, remove the index column and drop all blank columns
def readCSV(filename):
    df = pd.read_csv(filename,skip_blank_lines=True,index_col=False)
    df.dropna(how="all",inplace=True)
    return df
    
def connect(host_name,database_name,user_name,password):
    conn = psycopg2.connect(
    host = host_name,
    database = database_name,
    user = user_name,
    password = password)

    return conn


def storeData(table,df):
    engine = create_engine('postgresql://postgres:zs1178771178@localhost:5432/intern')
    df.to_sql(table,engine,if_exists='append',index=False)

def APIget(url):
    resp = requests.get(url)
    return resp

def jsonTodf(json_obj):
    keys = list(json_obj[0].keys())
    print(keys)
    df = pd.DataFrame(columns=keys)
    for i in range(0,len(json_obj)):
        currItem = json_obj[i]
        for j in range(len(keys)):
            df.loc[i,[keys[j]]] = currItem[keys[j]]
    return df

def readJSON(filename):
    data = json.load(open(filename))
    return data


