import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="10.235.81.97",
    database="CodeGames",
    user="postgres",
    password="Demo123$",
    port="8083"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

cursor.execute("Select * FROM customer_prod limit 10" )
rows = cursor.fetchall()


# Define the table name
table_name = "customer_qa"

# Get the column names from the table
cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
column_names = [desc[0] for desc in cursor.description]
#truncate the target table
cursor.execute(f"Delete from {table_name}")
# Generate the SQL query dynamically based on the column names
insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES "
# Generate the placeholders for the values
value_placeholders = ', '.join(['%s'] * len(column_names))
# Execute the insert query with the data
cursor.executemany(insert_query + f"({value_placeholders})", rows)
# Commit the transaction to save the changes
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()
