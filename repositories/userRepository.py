import sqlite3 

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password,database):
        con = sqlite3.connect(database)
        cur = con.cursor()
        res = cur.execute("SELECT ID FROM User WHERE email='"+email+"' and password='"+password+"'")
        data = res.fetchone()
        if(data==None):
            return [-1]
        else:
            return data
            
    @staticmethod
    def registerUser(email,password,database):
        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.execute("INSERT INTO User (email,password) VALUES (?,?)",(email,password))
        con.commit()

    @staticmethod
    def deleteUser(email,password,database):
        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.execute("DELETE FROM User WHERE email=? AND password=?;",(email,password))
        con.commit()