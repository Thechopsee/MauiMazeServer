import sqlite3 
import sys
sys.path.append('./models')
from GameRecord import GameRecord
from MoveRecord import MoveRecord

class RecordRepository:
    @staticmethod
    def saveMovesToDatabase(moves):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.executemany("INSERT INTO MoveRecord (percentagex,percentagey,hitwall,deltaTime,grID) VALUES (?,?,?,?,?)",moves)
        con.commit()
    @staticmethod
    def saveRecordtoDatabase(record):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        cur.execute("INSERT INTO GameRecord (mazeID,userID,timeInMilliSeconds,hitWallsCount,cellPathString) VALUES (?,?,?,?,?)",(record.get("mazeID"),record.get("userID"),record.get("timeInMilliSeconds"),record.get("hitWallsCount"),record.get("cellPathString")))
        con.commit()
        last_id = cur.lastrowid
        return last_id
    @staticmethod
    def loadRecordsbyMaze(mid):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM GameRecord WHERE mazeID="+str(mid))
        fetched=res.fetchall()
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0])
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4]))
            gameRecords.append(gr)
        return gameRecords
    @staticmethod
    def loadRecordsbyUser(uid):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM GameRecord WHERE userID="+str(uid))
        fetched=res.fetchall()
        gameRecords=[]
        for x in fetched:
            gr=GameRecord(x[0],x[1],x[2],x[3],x[4],x[5])
            fetchedmoves=RecordRepository.getMoves(x[0])
            for y in fetchedmoves:
                gr.records.append(MoveRecord(y[0],y[1],y[2],y[3],y[4]))
            gameRecords.append(gr)
        return gameRecords

    @staticmethod
    def getMoves(grid):
        con = sqlite3.connect("test.db")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM MoveRecord WHERE grID="+str(grid))
        
        if(res is None):
            return []
        else:
            return res.fetchall()