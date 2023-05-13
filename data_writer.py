import psycopg2
import pandas as pd
from psycopg2 import extras
from sqlalchemy import create_engine 

def write_to_target_db(host, database, user, password, port,table_name,data):
    conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
    )
    
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    # rows=data
    # Define the table name
    table_name = table_name

    #truncate the target table
    cursor.execute(f"Delete from {table_name}")
    # Create a database engine using SQLAlchemy
    engine = create_engine('postgresql+psycopg2://'+str(user)+':'+str(password)+'@'+str(host)+':'+str(port)+'/'+str(database))

    # Write the dataframe records to the existing table
    data.to_sql(table_name, engine, if_exists='append', index=False)
    # Commit the transaction to save the changes
    conn.commit()
    # Close the cursor and the database connection
    cursor.close()
    conn.close()