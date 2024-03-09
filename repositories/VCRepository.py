import sqlite3
from databaseServices.connectionProvider import ConnectionProvider
class VCRepository:
	@staticmethod
	def count_of_unused():
		sql='Select Count(*) from VerificationCodes WHERE used=0'
		adapter=ConnectionProvider().adapter
		return adapter.getOne(sql)
	@staticmethod
	def save_verification_code(code):
		sql='INSERT INTO VerificationCodes (code) VALUES (?)', code
		adapter=ConnectionProvider().adapter
		inserted_id = adapter.saveOne(sql,code)
		return inserted_id
		
	@staticmethod
	def updateCode(code):
		sql="UPDATE VerificationCodes SET used=1 WHERE code='"+str(code)+"'"
		adapter=ConnectionProvider().adapter
		adapter.getOne(sql)
		
	@staticmethod
	def isCodeTaken(codee):
		
		sql="SELECT used FROM VerificationCodes WHERE code='"+codee+"'"
		adapter=ConnectionProvider().adapter
		return adapter.getOne(sql)
