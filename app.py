from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai 
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_model_response(question,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    response = model.generate_content([prompt[0],question])
    return response.text

#Function to retreive the data from the database

import psycopg2
from psycopg2 import Error

def get_database_connection():
    try:
        connection = psycopg2.connect(
            database="inv_mng",
            user="postgres",
            password="1234", 
            host="localhost",
            port="5432"
        )
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

def execute_sql_query(sql_query):
    try:
        connection = get_database_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            records = cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            for record in records:
                print(record)
        return records
    except (Exception, Error) as error:
        print("Error while executing query:", error)
        return None

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name inv_mng and has the following tables with their columns  : 1) customer (customerid,name,email,phonenumber,address,createdat), 2) inventory (productid,productname,description,quantity,price,createdat), 3) orders (orderid,customerid,productid,quantity,orderdate,totalprice) \n\n. productid and customerid in the table orders are foreign key and queries can use joins if needed between orders and customer table and orders and inventory table. \n\n For example,\nExample 1 - How many order are placed with customerid=206?, 
    the SQL command will be something like this SELECT COUNT(*) FROM orders WHERE customerid=206;
    \nExample 2 - Tell me all about the customer with phonenumber 7987258065 and the orders they have placed?,
    the SQL command will be something like this SELECT c.*, o.* FROM customer c LEFT JOIN orders o ON c.customerid = o.customerid WHERE c.phonenumber='7987258065';
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

st.set_page_config(page_title="What would you like to know? ")
question=st.text_input("Input : ",key="input")
submit=st.button("Submit question")

if submit:
    response=get_gemini_model_response(question,prompt)
    print(response)

    data=execute_sql_query(response)
    st.subheader("Response is: ")
    if data is not None:
        for row in data:
            print(row)
            st.header(row)
    else:
        st.error("Error executing query. Please check the logs for details.")
