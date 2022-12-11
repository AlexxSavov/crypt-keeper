import requests
import pyodbc
import json

server = 'vertica1-bi-dev.pr1.points.com' 
database = 'pdw' 
username = 'etl_user' 
password = 'dbadmin_dev' 

data = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/tickers')

jsond = json.loads(data.content)

conn = pyodbc.connect('DSN=pdw-test')
cursor = conn.cursor()
cursor.execute("SELECT BATCH_KEY FROM AUDIT_CTRL.BATCH_KEY_CTRL")

# for row in cursor.fetchall():
#     print(row)

##jsondata = json.dumps(jsondata, indent=4)
