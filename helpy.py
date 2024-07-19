#!/usr/bin/env python
# -*- coding: utf8 -*-

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

		self.initialization_ok = None
		self.hex_integer = None
		self.paste = None
		self.payload = None

	@staticmethod
	def clear_buffer():
		pyperclip.copy(' ')

	def toaddr32(self, num): return '0x{0:08X}'.format(num)

	def generate_std_payload(self):
		assert self.hex_integer > 0

		tmp = self.hex_integer
		tmp = tmp - self.MAGIC

		tmp = tmp & 0x0FFFFFFF
		tmp = tmp + self.OP_EDIT_4BYTES

		arg1 = self.toaddr32(tmp)

		payload = f"_L {arg1} 0x01234567 // Helpy-automated: set address to 0x01234567"
		self.payload = payload

	def output_payload(self):
		pay = self.payload
		print("▒Output: \n"+pay)
		pyperclip.copy(pay)

	def initialize_variables(self):
		hex_string = self.paste

		if(hex_string[:1].isdigit() and (len(hex_string) > 6) and (int(hex_string, 16) > 0)):
			self.hex_integer = int(hex_string, 16)
			extended_test = self.hex_integer & 0xFFFFFFFFF0000000
			if(extended_test > 0):
				# Generate custom payload
				self.payload = "*Invalid PSP address: "+hex_string

				# Output payload
				self.output_payload()

				self.initialization_ok = False
				return ;
			self.initialization_ok = True
			return ;
		else:
			self.initialization_ok = False
			return ;

	def main(self):
		HOW_TO = """Just copy standard address to clipboard!"""

		print(self.PROGRAM_NAME+" "+"greets you!")
		print("How to: "+HOW_TO)

		try:
			while True:
				self.paste = pyperclip.paste().strip()
				self.initialize_variables()

				# check for valid input
				if(self.initialization_ok):
					print("*Valid PSP address: "+self.paste)
					# generate payload
					self.generate_std_payload()
					# print payload
					self.output_payload()
				time.sleep(0.1)
		except KeyboardInterrupt:
			print("\nExiting...", end="")

if __name__ == '__main__':
	helpy = Helpy()
	helpy.main()
