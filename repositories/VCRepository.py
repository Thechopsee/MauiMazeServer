from databaseServices.connectionProvider import ConnectionProvider

class VCRepository:
	@staticmethod
	def count_of_unused():
		sql='Select Count(*) from VerificationCodes WHERE used=0'
		adapter=ConnectionProvider().adapter
		return adapter.getOne(sql)
	@staticmethod
	def get_unused():
		sql='Select code from VerificationCodes WHERE used=0'
		adapter=ConnectionProvider().adapter
		return adapter.getMany(sql)
	@staticmethod
	def save_verification_code(code:str):
		sql="INSERT INTO VerificationCodes (code) VALUES (?)"
		adapter=ConnectionProvider().adapter
		inserted_id = adapter.saveOne(sql,(code,))
		return inserted_id
		
	@staticmethod
	def updateCode(code):
		sql="UPDATE VerificationCodes SET used=1 WHERE code=?"
		adapter=ConnectionProvider().adapter
		adapter.saveOne(sql,(code,))
		
	@staticmethod
	def isCodeTaken(codee):
		sql="SELECT used FROM VerificationCodes WHERE code='"+codee+"'"
		adapter=ConnectionProvider().adapter
		return adapter.getOne(sql)

