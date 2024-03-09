from databaseServices.databaseAdapter import DatabaseAdapter
import sqlite3 
class SqliteAdapter(DatabaseAdapter):
    def saveOne(self,sql,data) ->int:
        from databaseServices.connectionProvider import ConnectionProvider
        con = sqlite3.connect(ConnectionProvider().database)
        cur = con.cursor()
        cur.execute(sql,data)
        con.commit()
        last_id = cur.lastrowid
        con.close()
        return last_id

    def saveMany(self,sql,data):
        from databaseServices.connectionProvider import ConnectionProvider
        con = sqlite3.connect(ConnectionProvider().database)
        cur = con.cursor()
        cur.executemany(sql,data)
        con.commit()
        con.close()
    def getOne(self,sql):
        from databaseServices.connectionProvider import ConnectionProvider
        con = sqlite3.connect(ConnectionProvider().database)
        cur = con.cursor()
        res = cur.execute(sql)
        if(res is None):
            return -1
        else:
            return res.fetchone()
    def getMany(self,sql):
        from databaseServices.connectionProvider import ConnectionProvider
        con = sqlite3.connect(ConnectionProvider().database)
        cur = con.cursor()
        res = cur.execute(sql)
        if(res is None):
            return []
        else:
            return res.fetchall()
