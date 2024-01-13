import sqlite3 

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password):
        con = sqlite3.connect("../../test.db")
        cur = con.cursor()
        res = cur.execute("SELECT ID FROM User WHERE email='"+email+"' and password='"+password+"'")
        if(res.rowcount==-1):
            return -1
        else:
            return res.fetchone()
            
    @staticmethod
    def registerUser(email,password):
        con = sqlite3.connect("../../test.db")
        cur = con.cursor()
        cur.execute("INSERT INTO User (email,password) VALUES (?,?)",(email,password))
        con.commit()
