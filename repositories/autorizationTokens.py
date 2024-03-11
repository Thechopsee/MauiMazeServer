import sqlite3 
import sys
import time
sys.path.append('./models')
from tools.VerificationCodeGenerator import VerificationCodeGenerator
from databaseServices.connectionProvider import ConnectionProvider
class ATRepository:
    @staticmethod
    def createNewToken(id):
        kod=VerificationCodeGenerator.generate_verification_code()
        current_timestamp = int(time.time())
        adapter=ConnectionProvider().adapter
        sql="INSERT INTO AutorizationToken (token,userId,timestamp) VALUES(?,?,?)"
        adapter.saveOne(sql,(kod,id,current_timestamp))
        return kod
