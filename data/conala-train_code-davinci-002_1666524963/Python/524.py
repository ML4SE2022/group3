import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("SELECT * FROM stocks")

print(c.description)

# Output:
# (('date', None, None, None, None, None, None), ('trans', None, None, None, None, None, None), ('symbol', None, None, None, None, None, None), ('qty', None, None, None, None, None, None), ('price', None, None, None, None, None, None))