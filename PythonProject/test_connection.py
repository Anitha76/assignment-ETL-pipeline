import psycopg2

conn = psycopg2.connect(
    dbname="Sales_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

print("Connected successfully")

conn.close()