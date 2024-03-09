import sqlite3 
import datetime
from models.Maze import Maze
from models.Edge import Edge
from databaseServices.connectionProvider import ConnectionProvider
class MazeRepository:
    @staticmethod
    def saveEdgeToDatabase(edge):
        adapter=ConnectionProvider().adapter
        adapter.saveMany("INSERT INTO Edge (MazeID,Cell1,Cell2) VALUES (?,?,?)",edge)
    @staticmethod
    def saveMazetoDatabase(userid,type,StartCell,EndCell,Size):
        adapter=ConnectionProvider().adapter
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%dT%H:%M:%S")
        last_id = adapter.saveOne("INSERT INTO Maze (UserID,Type,CreationDate,StartCell,EndCell,Size) VALUES (?,?,?,?,?,?)",(userid,type,formatted_datetime,StartCell,EndCell,Size))
        return last_id
    @staticmethod
    def getMaze(id):
        sql="SELECT * FROM Edge WHERE MazeID="+str(id)
        adapter=ConnectionProvider().adapter
        res=adapter.getMany(sql)
        edges=[]
        for x in res :
            edges.append(Edge(x[2],x[3]))
        sql="SELECT * FROM Maze WHERE ID="+str(id)
        serialized_edges=[]
        resmaze=adapter.getOne(sql)
        for edge in edges:
                serialized_edges.append(edge.serialize())
        mazedto= {'size':resmaze[6],'startCell':resmaze[4],'endCell':resmaze[5],'edges':serialized_edges}
        return mazedto
    @staticmethod
    def getMazeList(id):
        adapter=ConnectionProvider().adapter
        sql="SELECT * FROM Maze WHERE UserID="+str(id)
        return adapter.getMany(sql)
    @staticmethod
    def getMazeCount(id):
        adapter=ConnectionProvider().adapter
        sql="SELECT Count(*) FROM Maze WHERE UserID="+str(id)
        return adapter.getOne(sql) 
    @staticmethod
    def countMazes(database) ->int:
        adapter=ConnectionProvider().adapter
        sql="SELECT COUNT(*) FROM Maze"
        return adapter.getOne(sql) 
