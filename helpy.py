import time

try:
	import pyperclip
except ModuleNotFoundError:
	print("Please install prerequisite,")
	print("```")
	print("pip install pyperclip")
	print("```")
	exit()

class Helpy:
	def __init__(self):
		self.PROGRAM_NAME = "Helpy"
		self.MAGIC = 0x08800000
		self.OP_EDIT_4BYTES = 0x20000000
		self.VAL = 1
		self.si = None
		self.paste = None

	def is_input_valid(self, s):
		if(s[:1].isdigit() and (len(s) > 6) and (int(s, 16) > 0)):
			return True
		return False

	def toaddr32(self, num): return '0x{0:08X}'.format(num)

	def gen_pay(self, s):
		self.si = int(s, 16)
		assert self.si > 0

		self.si = self.si - self.MAGIC

		test = self.si & 0xFFFFFFFFF0000000
		if(test > 0):
			print("(Warning) Invalid PSP address")

		self.si = self.si & 0x0FFFFFFF
		self.si = self.si + self.OP_EDIT_4BYTES
		arg1 = self.toaddr32(self.si)

		payload = f"_L {arg1} 0x01234567 // Helpy-automated: set address to 0x01234567"
		return payload

	def main(self):
		HOW_TO = """Just copy standard address to clipboard!"""

		print(self.PROGRAM_NAME+" "+"greets you!")
		print("How to: "+HOW_TO)

		try:
			while True:
				self.paste = pyperclip.paste().strip()

				# check for valid input
				if(self.is_input_valid(self.paste)):
					print("*Valid in: "+self.paste)
					# gen payload
					pay = self.gen_pay(self.paste)
					print("*Output: \n"+pay)
					pyperclip.copy(pay)
				time.sleep(0.1)
		except KeyboardInterrupt:
			print('Exiting...')

if __name__ == '__main__':
	helpy = Helpy()
	helpy.main()
