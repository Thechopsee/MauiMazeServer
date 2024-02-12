from databaseServices.databaseAdapter import DatabaseAdapter
import sqlite3 
class SqliteAdapter(DatabaseAdapter):
    def saveOne(self,database,sql,data) ->int:
        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.execute(sql,data)
        con.commit()
        last_id = cur.lastrowid
        con.close()
        return last_id

    def saveMany(self,database,sql,data):
        con = sqlite3.connect(database)
        cur = con.cursor()
        cur.executemany(sql,data)
        con.commit()
        con.close()
    def getOne(self,database,sql):
        con = sqlite3.connect(database)
        cur = con.cursor()
        res = cur.execute(sql)
        if(res is None):
            return -1
        else:
            return res.fetchone()
    def getMany(self,database,sql):
        con = sqlite3.connect(database)
        cur = con.cursor()
        res = cur.execute(sql)
        if(res is None):
            return []
        else:
            return res.fetchall()
