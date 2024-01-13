import sqlite3

class VCRepository:
	@staticmethod
	def save_verification_code(code):
		connection = sqlite3.connect("../../test.db")
		cursor = connection.cursor()

		cursor.execute('INSERT INTO VerificationCodes (code) VALUES (?)', (code,))
		
		connection.commit()
		connection.close()
		
	@staticmethod
	def updateCode(code):
		connection = sqlite3.connect("../../test.db")
		cursor = connection.cursor()

		cursor.execute("UPDATE VerificationCodes SET used=1 WHERE code='"+str(code)+"'")
		
		connection.commit()
		connection.close()

	@staticmethod
	def isCodeTaken(codee):
		con = sqlite3.connect("../../test.db")
		cur = con.cursor()
		res = cur.execute("SELECT used FROM VerificationCodes WHERE code='"+codee+"'")
		if(res is None):
			return -1
		else:
			return(int(res.fetchall()[0][0]))
