import sqlite3 
import sys
sys.path.append('./models')
from GameRecord import GameRecord
from MoveRecord import MoveRecord
from databaseServices.connectionProvider import ConnectionProvider

class RecordRepository:
    @staticmethod
    def saveMovesToDatabase(moves):
        sql="INSERT INTO MoveRecord (percentagex,percentagey,hitwall,deltaTime,grID,cell) VALUES (?,?,?,?,?,?)"
        adapter=ConnectionProvider().adapter
        adapter.saveMany(sql,moves)
    @staticmethod
    def saveRecordtoDatabase(record,adapter):
        sql="INSERT INTO GameRecord (mazeID,userID,timeInMilliSeconds,hitWallsCount,cellPathString) VALUES (?,?,?,?,?)"
        data=(record.get("mazeID"),record.get("userID"),record.get("timeInMilliSeconds"),record.get("hitWallsCount"),record.get("cellPathString"))

        last_id = adapter.saveOne(sql,data)
        return last_id
    @staticmethod
    def loadRecordByID(grid):
        sql="SELECT * FROM GameRecord WHERE grID="+str(grid)
        adapter=ConnectionProvider().adapter
        fetched=adapter.getMany(sql)
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0])
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4],y[6]))
            gameRecords.append(gr)
        return gameRecords
    @staticmethod
    def loadRecordsbyMaze(mid):
        sql="SELECT * FROM GameRecord WHERE mazeID="+str(mid)
        adapter=ConnectionProvider().adapter
        fetched=adapter.getMany(sql)
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0])
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4],y[6]))
            gameRecords.append(gr)
        return gameRecords
    @staticmethod
    def loadRecordsbyUser(uid):
        sql="SELECT * FROM GameRecord WHERE userID="+str(uid)
        adapter=ConnectionProvider().adapter
        fetched=adapter.getMany(sql)
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0])
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4],y[6]))
            gameRecords.append(gr)
        return gameRecords

    @staticmethod
    def getMoves(grid,adapter):
        sql="SELECT * FROM MoveRecord WHERE grID="+str(grid)
        return adapter.getMany(sql)
