import string
import random
class VerificationCodeGenerator:
	@staticmethod
	def generate_verification_code(length=8):
		characters = string.ascii_letters + string.digits
		return ''.join(random.choice(characters) for _ in range(length))
