import sqlite3
sqliteConnection = sqlite3.connect('instance\data.db')
sql_query = """SELECT * FROM user;"""
cursor = sqliteConnection.cursor()
cursor.execute(sql_query)
print(cursor.fetchall())