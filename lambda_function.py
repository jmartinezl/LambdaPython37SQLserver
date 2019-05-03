import pyodbc
import traceback
import sys

#Probado con Python 3.7 y SQL Server en RDS

server = 'rds-endpoint.us-west-2.rds.amazonaws.com'
database =  'DATABASE'
username = 'database_user'
password = 'p@ssw0rd'
driver = 'ODBC Driver 17 for SQL Server'
port = '9000'


def lambda_handler(event, context):
    # TODO implement
    try:
        connection_string = 'DRIVER={driver};SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'.format( driver=driver,server=server, port=port, database=database, username=username, password=password)
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("select @@version;")
        row = cursor.fetchone()
        
        print(row[0])
    except Exception:
        traceback.print_exc()
        sys.exit()