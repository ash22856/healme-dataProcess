import pandas as pd
import utils as ut

def dropNaCol(df):
    df.dropna(axis='columns',how='all',inplace=True)
    return df

def dropNaRow(df):
    df.dropna(axis='index',how='all',inplace=True)
    return df

def dropNaPKRow(df,hostname,database_name,user_name,password,tablename):
    q = ('SELECT a.attname, format_type(a.atttypid, a.atttypmod) AS data_type FROM pg_index i'
        'JOIN   pg_attribute a ON a.attrelid = i.indrelid'
        'AND a.attnum = ANY(i.indkey)'
        'WHERE  i.indrelid = ?::regclass'
        'AND    i.indisprimary;')
    conn = ut.connect(hostname,database_name,user_name,password)
    cur = conn.cursor()
    PKs = cur.execute(q,tablename)
    df.dropna(axis='index',how='any',subset=(PKs),inplace=True)
    return df

def fillNAZero(df):
    df.fillna(0,inplace=True)
    return df

def typeCast(df,colname,newType):
    df[colname] = df[colname].astype(newType)
    return df

def fillNAprevious(df):
    df.fillna(method='pad',inplace=True)
    return df

def fillNAcoming(df):
    df.fillna(method='bfill',inplace=True)
    return df