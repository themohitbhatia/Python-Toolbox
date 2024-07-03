import pandas as pd
from sqlalchemy import create_engine
import urllib
import pyodbc


server = 'server'
database = 'database'
username = 'username'
password = 'password'
driver = '{ODBC Driver 17 for SQL Server}'


# Print available ODBC drivers to verify the correct driver name
print("Available ODBC drivers:")
print(pyodbc.drivers())


# Ensure the correct ODBC driver is used
driver = 'ODBC Driver 17 for SQL Server'

# Create the connection string
connection_string = (
    f'DRIVER={{{driver}}};'  # Notice the triple braces {{}} to include braces in f-string
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)
# Ensure the correct ODBC driver is used

# Encode the connection string to be URL safe
params = urllib.parse.quote_plus(connection_string)

# Create the engine
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')


tables = pd.read_sql('SELECT table_name FROM information_schema.tables', engine)


table = pd.read_sql('select * from table_name', engine)