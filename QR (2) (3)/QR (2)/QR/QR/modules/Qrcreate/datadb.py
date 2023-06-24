import sqlite3
import customtkinter as ctk



connect = sqlite3.connect("qrbasa.db")
data = connect.cursor()

table = "CREATE TABLE IF NOT EXISTS Users (ID INTEGER PRIMARY KEY)"


data.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  login TEXT,
                  password TEXT)''')
#name_user_query = '''ALTER TABLE Users ADD COLUMN name TEXT'''
#qr_user_query = '''ALTER TABLE Users ADD COLUMN qr_data TEXT'''

#data.execute(name_user_query)
#data.execute(qr_user_query)

data.execute(table)

# text_column = '''ALTER TABLE Users ADD COLUMN text TEXT'''

# data.execute(text_column)