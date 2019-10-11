import pyodbc
import json
server = 'truss.database.windows.net'
database = 'titanicData'
username = 'trushal'
password = 'TRuss712#'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select * from mainData")
dataset = cursor.fetchall()
print(dataset)

