import sqlite3

connection= sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS properties (id INTEGER PRIMARY KEY, location text, type text, floor int, price int, bed int, bath int, kitchen int, garage int, agent text, phone int, review text)"
cursor.execute(create_table)

connection.commit()

connection.close()