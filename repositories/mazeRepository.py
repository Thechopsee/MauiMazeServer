import sqlite3 
import datetime
from models.Maze import Maze
from models.Edge import Edge
class MazeRepository:
    @staticmethod
    def saveEdgeToDatabase(edge,database):
        global adapter
        adapter.saveMany(database,"INSERT INTO Edge (MazeID,Cell1,Cell2) VALUES (?,?,?)",edge)
    @staticmethod
    def saveMazetoDatabase(userid,type,StartCell,EndCell,Size,database):
        global adapter
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%dT%H:%M:%S")
        last_id = adapter.saveOne(database,"INSERT INTO Maze (UserID,Type,CreationDate,StartCell,EndCell,Size) VALUES (?,?,?,?,?,?)",(userid,type,formatted_datetime,StartCell,EndCell,Size))
        return last_id
    @staticmethod
    def getMaze(id,database):
        sql="SELECT * FROM Edge WHERE MazeID="+str(id)
        global adapter
        res=adapter.getMany(database,sql)
        edges=[]
        for x in res :
            edges.append(Edge(x[2],x[3]))
        sql="SELECT * FROM Maze WHERE ID="+str(id)
        serialized_edges=[]
        resmaze=adapter.getOne(database,sql)
        for edge in edges:
                serialized_edges.append(edge.serialize())
        mazedto= {'size':resmaze[6],'startCell':resmaze[4],'endCell':resmaze[5],'edges':serialized_edges}
        return mazedto
    @staticmethod
    def getMazeList(id,database):
        global adapter
        sql="SELECT * FROM Maze WHERE UserID="+str(id)
        return adapter.getMany(database,sql)
    @staticmethod
    def getMazeCount(id,database):
        global adapter
        sql="SELECT Count(*) FROM Maze WHERE UserID="+str(id)
        return adapter.getOne(database,sql) 
    @staticmethod
    def countMazes(database) ->int:
        global adapter
        sql="SELECT COUNT(*) FROM Maze"
        return adapter.getOne(database,sql) 
