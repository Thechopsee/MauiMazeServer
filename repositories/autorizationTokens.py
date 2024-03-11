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
        sql="INSERT INTO AT (token,userId,timestamp) VALUES(?,?,?)"
        adapter.saveOne(sql,(kod,id,current_timestamp))
        return kod

    def checkToken(token,role):
        sql="Select * from AT where token='"+token+"'"
        adapter=ConnectionProvider().adapter
        res=adapter.getOne(sql)
        from repositories.userRepository import UserRepository
        current_timestamp = int(time.time())
        if(res is not None):
                if(res[2]>current_timestamp+3600):
                        return False
                else:
                        if(UserRepository.getUserRole()>=role):
                            return True
                
        return False
