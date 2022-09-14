from operator import index
import psycopg2
import pandas as pd
import utils
from sqlalchemy import create_engine


def main():
    print("Welcome! Please select an option: ")
    option = input("1.store   2.View   3.Add   4.Delete   5.Modify ")
    if option=='1':
        table = input("Please enter the table name: ")
        filepath = input("please enter the csv file path: ")
        try:
            df = getData(filepath)
            storeData(table,df)
        except (Exception):
            print("Please ensure the table name and path are correct")
        else:
            print("Value stored")




