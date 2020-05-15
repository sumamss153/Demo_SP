import pyodbc
import pandas as pd

def main():

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=IN2396424W1\SQLEXPRESS;'
                      'Database=Test_DB_SSS;'
                      'Trusted_Connection=yes;')
    spname = "GetProductDesc"
    ret_data = pd.read_sql('EXEC [dbo].' + spname,conn)
    print(ret_data)

main()