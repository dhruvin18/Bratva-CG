from flask import Flask, jsonify, request
from Data_Masker import check_database_connection
from datamasking import datamask
from data_writer import write_to_target_db
import psycopg2
from psycopg2 import OperationalError
from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)

@app.route('/Data_mask', methods=['POST'])
def Check_Connection():
    print(str(datetime.now())+ "Request received")
    host=request.form['host']
    database = request.form['database']
    user = request.form['user']
    password = request.form['password']
    port = request.form['port'] 
    try:
        print(str(datetime.now())+ ": DB connection Start")   
        conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
        curr=conn.cursor()
        print(str(datetime.now())+ ": DB connection End")   
        curr.execute("Select * FROM customer_prod" )
        rows = curr.fetchall()
        print(str(datetime.now())+ ": Data Fetch ENd")   
        column_headers = [desc[0] for desc in curr.description]
        columns = request.form['columns']
        types = request.form['types']
        print(str(datetime.now())+ ": Data Masking Start")   
        data=datamask(rows,column_headers,columns,types)
        print(str(datetime.now())+ ": Data Masking end")   
        target_host=request.form['target_host']
        target_database = request.form['target_database']
        target_user = request.form['target_user']
        target_password = request.form['target_password']
        target_port = request.form['target_port']
        table_name = request.form['table_name']
        print(str(datetime.now())+ ": Write Start")   
        write_to_target_db(target_host,target_database,target_user,target_password,target_port,table_name,data)
        print(str(datetime.now())+ ": Write End")   
        response = {'success': True}
        return jsonify(response)
    except OperationalError:
        response = {'success': False}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
