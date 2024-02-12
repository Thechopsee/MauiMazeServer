import sqlite3 

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password,database,adapter):
        sql="SELECT ID FROM User WHERE email='"+email+"' and password='"+password+"'"
        return adapter.getOne(database,sql)
            
    @staticmethod
    def registerUser(email,password,database,adapter):
        sql="INSERT INTO User (email,password) VALUES (?,?)"
        return adapter.saveOne(database,sql,(email,password))

    @staticmethod
    def deleteUser(email,password,database,adapter):
        sql="DELETE FROM User WHERE email=? AND password=?;"
        adapter.saveOne(database,sql,(email,password))