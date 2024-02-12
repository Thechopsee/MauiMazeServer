import sqlite3

class VCRepository:
	@staticmethod
	def count_of_unused(database):
		connection = sqlite3.connect(database)
		cursor = connection.cursor()

		res=cursor.execute('Select Count(*) from VerificationCodes WHERE used=0')
		if(res is None):
			return -1
		else:
			return(int(res.fetchall()[0][0]))
	@staticmethod
	def save_verification_code(code,database):
		connection = sqlite3.connect(database)
		cursor = connection.cursor()

		cursor.execute('INSERT INTO VerificationCodes (code) VALUES (?)', (code,))
		
		connection.commit()
		inserted_id = cursor.lastrowid
		connection.close()
		return inserted_id
		
	@staticmethod
	def updateCode(code,database):
		connection = sqlite3.connect(database)
		cursor = connection.cursor()

		cursor.execute("UPDATE VerificationCodes SET used=1 WHERE code='"+str(code)+"'")
		
		connection.commit()
		connection.close()

	@staticmethod
	def isCodeTaken(codee,database):
		con = sqlite3.connect(database)
		cur = con.cursor()
		res = cur.execute("SELECT used FROM VerificationCodes WHERE code='"+codee+"'")
		if(res is None):
			return -1
		else:
			return(int(res.fetchall()[0][0]))
