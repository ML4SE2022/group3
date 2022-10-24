import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("SELECT * FROM COMPANY WHERE SALARY > %s", (1000,))
rows = cur.fetchall()
for row in rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()