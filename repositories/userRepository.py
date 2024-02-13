import sqlite3 

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password,database,adapter):
        sql="SELECT * FROM User WHERE email='"+email+"' and password='"+password+"'"
        res=adapter.getOne(database,sql)
        if(res is  None):
            response = {'id': -1,'role': -1,'name':'-1'}
        else:
            role=0
            if(res[3]==1):
                role=2
            elif(res[4]==1):
                role=1
            response = {'id': res[0],'role': role,'name':res[1]}
        return response
            
    @staticmethod
    def registerUser(email,password,database,adapter):
        sql="INSERT INTO User (email,password) VALUES (?,?)"
        return adapter.saveOne(database,sql,(email,password))

    @staticmethod
    def deleteUser(email,password,database,adapter):
        sql="DELETE FROM User WHERE email=? AND password=?;"
        adapter.saveOne(database,sql,(email,password))