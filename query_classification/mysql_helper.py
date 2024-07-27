import mysql.connector
from mysql.connector import Error
import pandas as pd

class _mysql:
    connection=None
    show_column=[]
    show_table=None
    def __init__(self,host,port,user,password,database):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
        
    def connect_(self):
        if(self.connection is not None and self.connection.is_connected()):
            pass
        else:    
            self.connection = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database,raise_on_warnings=False)

    def close_(self):
        if self.connection.is_connected():
            self.connection.close()
        elif (self.connection is None ):
            pass

    def fetch_column(self,tableName):
        self.show_column=[]
        cursor = None
        try:
            self.connect_()
            cursor = self.connection.cursor()
            cursor.execute("SHOW columns FROM `"+ tableName +"`;")
            result=cursor.fetchall()
            for i in result:
                self.show_column.append(i[0])
        except Exception as e:
            print(e)
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
    
    def fetch_table(self,tableName):
        cursor = None
        try:
            #self.fetch_column()
            self.connect_()
            cursor = self.connection.cursor()
            cursor.execute("select * from `"+ tableName +"`;")
            result=cursor.fetchall()
            self.show_table=pd.DataFrame(result,columns=self.show_column)
        except Exception as e:
            print(e)
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()

    def fetch_query(self,query):
        cursor = None
        try:
            #self.show_column=[]
            self.connect_()
            cursor = self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            if len(self.show_column) ==0:
                return(result)
            else:
                self.show_table=pd.DataFrame(result,columns=self.show_column)
        except Exception as e:
            print(e)
        finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()

    # def push_data(self,query):
    #     cursor = None
    #     try:
    #         self.connect_()
    #         cursor = self.connection.cursor()
    #         cursor.execute(query)
    #         self.connection.commit()
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         if self.connection.is_connected():
    #             cursor.close()
    #             self.connection.close()


    def push_data(self, query, values=None):
        cursor = None
        try:
            self.connect_()
            cursor = self.connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()