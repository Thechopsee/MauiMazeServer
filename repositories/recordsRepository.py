import sqlite3 
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
        cur.execute("INSERT INTO GameRecord (mazeID,userID,timeInMilliSeconds,hitWallsCount,cellPathString) VALUES (?,?,?,?,?)",(record.mazeID,record.user.ID,record.timeInMilliSeconds,record.hitWallsCount,record.cellPathString))
        con.commit()
        last_id = cur.lastrowid
        return last_id