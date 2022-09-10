import mysql.connector
from mysql.connector import Error
import pandas as pd
import sqlite3
import streamlit as st
# import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

def app():
        

        st.title("AppMela Dashboard")


        cols = st.columns([.333, .333, .333])

        option2 = st.selectbox(
        'How many rows you would like to display',
        ('10', '50', '100'))


        placeholder = st.empty()    


        try:
                def init_connection():
                    return mysql.connector.connect(**st.secrets["mysql"])
            
                conn = mysql.connector.connect(host='localhost',
                                                        database='appmela',
                                                        user='root',
                                                        password='india@123')

                conn = init_connection()
                
                if conn.is_connected():
                        db_Info = conn.get_server_info()
                        print("Connected to MySQL Server version ", db_Info)
                        cursor = conn.cursor(buffered = True)
                        record = cursor.execute('''select vid, apprenticemelacenter, stateName, DistrictName, from 
                                       vacancy_details1''')
                        for record in rows:
                                if record.with_rows: 
                                        record = cursor.fetchall()
                                        df = pd.DataFrame(record, columns =['tot_stud', 'tot_est', 'state', 'district'
                                                                        ])
                        print(df)
                        
        except Error as e:
                print("Error while connecting to MySQL", e)
                        