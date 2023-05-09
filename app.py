import psycopg2

conn = psycopg2.connect(
    host="10.235.81.97",
    database="cams_app_monitoring",
    user="postgres",
    password="Demo123$",
    port="8083"
)

cur = conn.cursor()
cur.execute("select * from \"appMonitoring\".app_hlth ah where app_name like '%Passport%'; ")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
