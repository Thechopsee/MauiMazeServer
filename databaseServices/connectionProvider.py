from databaseServices.databaseAdapter import DatabaseAdapter 
from databaseServices.sqliteAdapter import SqliteAdapter
import os
class ConnectionProvider:
    _instance = None
    adapter: DatabaseAdapter
    database :str
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            db_type=os.environ.get('database_type')
            if(db_type == 'SQLITE'):
                cls._instance.adapter=SqliteAdapter()
            cls._instance.database=os.environ.get('database_connection_string')
        return cls._instance