import sqlite3 
import datetime
class MazeRepository:
    @staticmethod
    def saveEdgeToDatabase(edge):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.executemany("INSERT INTO Edge (MazeID,Cell1,Cell2) VALUES (?,?,?)",edge)
        con.commit()
    @staticmethod
    def saveMazetoDatabase(userid,type):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        now = datetime.datetime.now()

        formatted_datetime = now.strftime("%Y-%m-%dT%H:%M:%S")
        cur.execute("INSERT INTO Maze (UserID,Type,CreationDate) VALUES (?,?,?)",(userid,type,formatted_datetime))
        con.commit()
        last_id = cur.lastrowid
        return last_id
    @staticmethod
    def getMaze(id):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM Edge WHERE MazeID="+str(id))
        
        if(res is None):
            return []
        else:
            return res.fetchall()
    @staticmethod
    def getMazeList(id):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM Maze WHERE UserID="+str(id))
        if(res is None):
            return []
        else:
            return res.fetchall()
    @staticmethod
    def getMazeCount(id):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.execute("SELECT Count(*) FROM Maze WHERE UserID="+str(id))
        count = cur.fetchone()[0]
        print(count)
        con.close()
        return count
    @staticmethod
    def countMazes() ->int:
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM Maze")
        count = cur.fetchone()[0]
        print(count)
        con.close()
        return count
