import mysql.connector

conn = mysql.connector.connect(host = 'localhost' , database= 'PythonAutomation', user = 'root', password = 'root1234')

print(conn.is_connected())

cur = conn.cursor()
cur.execute('use APIDevelop')
cur.execute('select * from Books')
row = cur.fetchall()
print(row)