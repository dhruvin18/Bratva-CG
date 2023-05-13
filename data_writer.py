import psycopg2
import pandas as pd
from psycopg2 import extras

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
    rows=data
    # Define the table name
    table_name = table_name
    # Get the column names from the table
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
    column_names = [desc[0] for desc in cursor.description]
    #truncate the target table
    cursor.execute(f"Delete from {table_name}")
    # Generate the SQL query dynamically based on the column names
    insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES "
    # Generate the placeholders for the values
    value_placeholders = ', '.join(['%s'] * len(column_names))
    rows = data.values.tolist()  # Convert dataframe to a list of lists
    # Execute the insert query with the data
    cursor.executemany(insert_query + f"({value_placeholders})", rows)
    # Commit the transaction to save the changes
    conn.commit()
    # Close the cursor and the database connection
    cursor.close()
    conn.close()