import sqlite3
import pandas as pd
df=pd.read_csv('C:/Users/Celal/Documents/pythonProject/python_temelleri/Pandas/datasets/Cars.csv')
df=pd.read_json('C:/Users/Celal/Documents/pythonProject/python_temelleri/Pandas/datasets/sample.json')

connection = sqlite3.connect("C:/Users/Celal/Documents/pythonProject/python_temelleri/Pandas/datasets/sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection)
df=pd.read_csv('C:/Users/Celal/Documents/pythonProject/python_temelleri/Pandas/datasets/Cars.csv')
print(df.columns)
