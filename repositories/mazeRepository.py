import sqlite3 
import datetime
class MazeRepository:
    @staticmethod
    def saveEdgeToDatabase(edge,database,adapter):
        adapter.saveMany(database,"INSERT INTO Edge (MazeID,Cell1,Cell2) VALUES (?,?,?)",edge)
    @staticmethod
    def saveMazetoDatabase(userid,type,StartCell,EndCell,Size,database,adapter):
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%dT%H:%M:%S")
        last_id = adapter.saveOne(database,"INSERT INTO Maze (UserID,Type,CreationDate,StartCell,EndCell,Size) VALUES (?,?,?,?,?,?)",(userid,type,formatted_datetime,StartCell,EndCell,Size))
        return last_id
    @staticmethod
    def getMaze(id,database,adapter):
        sql="SELECT * FROM Edge WHERE MazeID="+str(id)
        return adapter.getMany(database,sql)
    @staticmethod
    def getMazeList(id,database,adapter):
        sql="SELECT * FROM Maze WHERE UserID="+str(id)
        return adapter.getMany(database,sql)
    @staticmethod
    def getMazeCount(id,database,adapter):
        sql="SELECT Count(*) FROM Maze WHERE UserID="+str(id)
        return adapter.getOne(database,sql) 
    @staticmethod
    def countMazes(database,adapter) ->int:
        sql="SELECT COUNT(*) FROM Maze"
        return adapter.getOne(database,sql) 
