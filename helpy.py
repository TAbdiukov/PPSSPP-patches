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
		self.payload = None

	@staticmethod
	def clear_buffer():
		pyperclip.copy(' ')

	def gen_si(self, s):
		self.si = int(s, 16)

	def toaddr32(self, num): return '0x{0:08X}'.format(num)

	def gen_std_pay(self):
		assert self.si > 0

		tmp = self.si
		tmp = tmp - self.MAGIC

		tmp = tmp & 0x0FFFFFFF
		tmp = tmp + self.OP_EDIT_4BYTES

		arg1 = self.toaddr32(self.si)

		payload = f"_L {arg1} 0x01234567 // Helpy-automated: set address to 0x01234567"
		self.payload = payload

	def output_pay(self):
		pay = self.payload
		print("▒Output: \n"+pay)
		pyperclip.copy(pay)

	def is_input_valid(self, s):
		if(s[:1].isdigit() and (len(s) > 6) and (int(s, 16) > 0)):
			self.gen_si(s)
			test = self.si & 0xFFFFFFFFF0000000
			if(test > 0):
				self.payload = "*Invalid PSP address: "+s
				self.output_pay()
				
				return False
			return True
		return False

	def main(self):
		HOW_TO = """Just copy standard address to clipboard!"""

		print(self.PROGRAM_NAME+" "+"greets you!")
		print("How to: "+HOW_TO)

		try:
			while True:
				self.paste = pyperclip.paste().strip()

				# check for valid input
				if(self.is_input_valid(self.paste)):
					print("*Valid PSP address: "+self.paste)
					# generate payload
					self.gen_std_pay()
					# print payload
					self.output_pay()
				time.sleep(0.1)
		except KeyboardInterrupt:
			print('\nExiting...')

if __name__ == '__main__':
	helpy = Helpy()
	helpy.main()
