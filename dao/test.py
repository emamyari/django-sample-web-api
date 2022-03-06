from Model.Users import User
from dao.sqlBase import sqlbase



def insertFooddb(Name,Type,Price,Des):
    try:
        #connect to database
        sqlBase = sqlbase()
        connection, cursor = sqlBase.getConnection()

        #Run command
        cursor.execute(f"insert into Fouds (Name,Price,Type,Description) Values ('{Name}',{Price},{Type},'{Des}') ")
        connection.commit()

        cursor.close()
        connection.close()
        return True
    except:
        return False

