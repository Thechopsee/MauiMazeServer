import sqlite3

class VCRepository:
	@staticmethod
	def count_of_unused(database,adapter):
		sql='Select Count(*) from VerificationCodes WHERE used=0'
		return adapter.getOne(database,sql)
	@staticmethod
	def save_verification_code(code,database,adapter):
		sql='INSERT INTO VerificationCodes (code) VALUES (?)', code
		inserted_id = adapter.saveOne(database,sql,code)
		return inserted_id
		
	@staticmethod
	def updateCode(code,database,adapter):
		sql="UPDATE VerificationCodes SET used=1 WHERE code='"+str(code)+"'"
		adapter.getOne(database,sql)
		
	@staticmethod
	def isCodeTaken(codee,database,adapter):
		
		sql="SELECT used FROM VerificationCodes WHERE code='"+codee+"'"
		return adapter.getOne(database,sql)
