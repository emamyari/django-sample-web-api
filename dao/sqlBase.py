import pyodbc


class sqlbase():
    def getConnection(self):
        connection=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=emamyari;UID=sa;PWD=111')
        cursor=connection.cursor()
        return connection,cursor
