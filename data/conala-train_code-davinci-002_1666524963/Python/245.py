import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='127.0.0.1',
                              database='employees')
cursor = cnx.cursor()

# Disable query cache
cursor.execute("SET SESSION query_cache_type = OFF")

# Execute query
cursor.execute("SELECT * FROM employees LIMIT 10")

# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
cnx.close()