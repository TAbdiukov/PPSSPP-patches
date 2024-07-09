#!/usr/bin/env python

import re
import sys

def toaddr32(num): return '{0:08X}'.format(num)

def convert_decimal_to_hex(file_path):
	with open(file_path, 'r') as file:
		data = file.read()

	# Find all decimal numbers defined by `162 XX XX XX` or `163 XX XX XX` (decimal)
	pattern = r'\b(162\d{6}|163\d{6})\b'
	matches = re.findall(pattern, data)

	for match in matches:
		# Hello helpy.py
		hex_value = toaddr32(int(match))
		data = data.replace(match, hex_value)

	# Write back
	with open(file_path, 'w') as file:
		file.write(data)

def main():
	if len(sys.argv) < 2:
		print("Error: No file path provided.")
		print("Usage: python script.py <index.md>")
		sys.exit()

	filename = sys.argv[1]

	convert_decimal_to_hex(filename)

if __name__ == '__main__':
	main()
