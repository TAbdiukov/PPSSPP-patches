#!python3

# Python 3.6+ required.

# Before use, run:
# pip install pyperclip

import time

try:
	import pyperclip
except ModuleNotFoundError:
	print("Please install prerequisite,")
	print("```")
	print("pip install pyperclip")
	print("```")
	exit()

"""
it is a simple as subtracting 0x08800000 are you sure you have the correct base address
_L 0x203B3B58 0x3F800000
"""

PROGRAM_NAME = "Helpy"
MAGIC = 0x08800000
OP_EDIT_4BYTES = 0x20000000
VAL = 1

def is_input_valid(s):
	if(s[:1].isdigit() and (len(s) > 6) and (int(s, 16) > 0)):
		return True
	return False

def toaddr32(num): return '0x{0:08X}'.format(num)


def gen_pay(s):
	si = int(s, 16)
	assert si > 0
	
	si = si - MAGIC
	
	test = si & 0xFFFFFFFFF0000000
	if(test > 0):
		print("(Warning) Invalid PSP address")
		
	si = si & 0x0FFFFFFF
	si = si + OP_EDIT_4BYTES
	arg1 = toaddr32(si)
	
	payload = f"_L {arg1} 0x01234567 // Helpy-automated: set address to 0x01234567"
	return payload

def main():
	HOW_TO = """Just copy standard address to clipboard!"""
	
	print(PROGRAM_NAME+" "+"greets you!")
	print("How to: "+HOW_TO)
	
	try:
		while True:
			paste = pyperclip.paste().strip()
			
			# check for valid input 
			if(is_input_valid(paste)):
				print("*Valid in: "+paste)
				# gen payload
				pay = gen_pay(paste)
				print("*Output: \n"+pay)
				pyperclip.copy(pay)
			time.sleep(0.1)
	except KeyboardInterrupt:
		print('Exiting...')


if __name__ == '__main__':
	main()
