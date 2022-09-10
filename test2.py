import pyodbc
import pandas.io.sql as psql
import mysql.connector
from mysql.connector import Error
import streamlit as st
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}',host='localhost',
#                                          database='appmela',
#                                          user='root',
#                                          password='india@123')
# [x for x in pyodbc.drivers() if x.startswith("Microsoft Access Driver")]
server = 'localhost',
database = 'appmela'
username = 'root'
password = 'india@123'

con = mysql.connector.connect(host='localhost',
                                            database='appmela',
                                            user='root',
                                            password='india@123')

# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = con.cursor()
sql_query = """select count(id) from student_registration; select count(id) from establishment; select stateName from state; select Districts_name from districts;"""

cursor.execute(sql_query)

for row in cursor:
    print(row)
# sql = """select count(id) from student_registration; select count(id) from establishment; select stateName from state; select Districts_name from districts;"""
    
# df = psql.frame_query(sql, cnxn)
# print(df)
# cnxn.close()

