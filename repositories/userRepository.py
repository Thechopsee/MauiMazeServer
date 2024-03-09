import sqlite3 
from databaseServices.connectionProvider import ConnectionProvider

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password):
        sql="SELECT * FROM User WHERE email='"+email+"' and password='"+password+"'"
        adapter=ConnectionProvider().adapter
        res=adapter.getOne(sql)
        if(res is  None):
            response = {'id': -1,'role': -1,'email':'-1','firstname':'a','lastname':'a' }
        else:
            role=0
            if(res[3]==1):
                role=2
            elif(res[4]==1):
                role=1
            response = {'id': res[0],'role': role,'email':res[1],'firstname':res[5],'lastname':res[6]}
        return response
    @staticmethod        
    def getUsersForResearcher():
        sql="SELECT * FROM User WHERE researcher=0 and admin=0"
        adapter=ConnectionProvider().adapter
        res=adapter.getMany(sql)
        users=[]
        for x in res:
            role=0
            userDTO = {'id': x[0],'role': role,'email':x[1],'firstname':x[5],'lastname':x[6]}
            users.append(userDTO)
        return users
    @staticmethod
    def registerUser(email,password):
        sql="INSERT INTO User (email,password) VALUES (?,?)"
        adapter=ConnectionProvider().adapter
        return adapter.saveOne(sql,(email,password))

    @staticmethod
    def deleteUser(email,password):
        sql="DELETE FROM User WHERE email=? AND password=?;"
        adapter=ConnectionProvider().adapter
        adapter.saveOne(sql,(email,password))
