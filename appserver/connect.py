import pymssql

server = **DELETED**
database = **DELETED**
username = **DELETED**
password = **DELETED**


cnxn = pymssql.connect(server=server,
                       database=database,
                       user=username,
                       password=password)

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Users;')
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
