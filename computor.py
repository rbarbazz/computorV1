import sys
import argparse
import re

def get_input():
	parser = argparse.ArgumentParser()
	parser.add_argument('equation', help='Polynomial equation to be solved')
	return parser.parse_args().equation

def rm_wspaces(raw_input):
	return re.sub(r'\s+', '', raw_input)

def get_terms(str):
	matchs = re.search(r'([+-]?\d+(\.)?(?(2)\d+)\*X\^0)|([+-]?\d+(\.)?(?(4)\d+)\*X\^1)|([+-]?\d+(\.)?(?(6)\d+)\*X\^2)', str)
	print(matchs.group(3))

class Equation:
	def __init__(self, raw_input):
		input = rm_wspaces(raw_input)
		self.left = input.split('=')[0]
		self.right = input.split('=')[1]



raw_input = get_input()
equals_count = raw_input.count('=')
if equals_count != 1:
	sys.exit('Wrong format: found {} equals sign'.format(equals_count))
equation = Equation(raw_input)
get_terms(equation.left)