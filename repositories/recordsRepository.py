import sqlite3 
import sys
sys.path.append('./models')
from GameRecord import GameRecord
from MoveRecord import MoveRecord

class RecordRepository:
    @staticmethod
    def saveMovesToDatabase(moves,database,adapter):
        sql="INSERT INTO MoveRecord (percentagex,percentagey,hitwall,deltaTime,grID,cell) VALUES (?,?,?,?,?,?)"
        adapter.saveMany(database,sql,moves)
    @staticmethod
    def saveRecordtoDatabase(record,database,adapter):
        sql="INSERT INTO GameRecord (mazeID,userID,timeInMilliSeconds,hitWallsCount,cellPathString) VALUES (?,?,?,?,?)"
        data=(record.get("mazeID"),record.get("userID"),record.get("timeInMilliSeconds"),record.get("hitWallsCount"),record.get("cellPathString"))

        last_id = adapter.saveOne(database,sql,data)
        return last_id
    @staticmethod
    def loadRecordByID(grid,database,adapter):
        sql="SELECT * FROM GameRecord WHERE grID="+str(grid)
        fetched=adapter.getMany(database,sql)
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0],database,adapter)
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4],y[6]))
            gameRecords.append(gr)
        return gameRecords
    @staticmethod
    def loadRecordsbyMaze(mid,database,adapter):
        sql="SELECT * FROM GameRecord WHERE mazeID="+str(mid)
        fetched=adapter.getMany(database,sql)
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0],database,adapter)
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4],y[6]))
            gameRecords.append(gr)
        return gameRecords
    @staticmethod
    def loadRecordsbyUser(uid,database,adapter):
        sql="SELECT * FROM GameRecord WHERE userID="+str(uid)
        fetched=adapter.getMany(database,sql)
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0],database,adapter)
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4],y[6]))
            gameRecords.append(gr)
        return gameRecords

    @staticmethod
    def getMoves(grid,database,adapter):
        sql="SELECT * FROM MoveRecord WHERE grID="+str(grid)
        return adapter.getMany(database,sql)
