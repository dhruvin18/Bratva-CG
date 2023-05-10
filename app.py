import psycopg2

conn = psycopg2.connect(
    host="10.235.81.97",
    database="CodeGames",
    user="postgres",
    password="Demo123$",
    port="8083"
)

cur = conn.cursor()
cur.execute("Select * FROM customer_prod limit 10" )
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()

