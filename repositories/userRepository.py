import sqlite3 

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        res = cur.execute("SELECT ID FROM User WHERE email='"+email+"' and password='"+password+"'")
        if(res is None):
            return -1
        else:
            return res.fetchone()