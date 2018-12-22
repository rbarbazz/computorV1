import sys
import argparse
import re

def get_input():
	parser = argparse.ArgumentParser(description='Solve a polynomial equation up to degree 2')
	parser.add_argument('equation', help='Format: \"n * X^[0-2]\"')
	return re.sub(r'\s+', '', parser.parse_args().equation)

class Equation:
	def __init__(self, raw_input):
		self.left = input.split('=')[0]
		self.right = input.split('=')[1]
		self.terms = {0: 0, 1: 0, 2: 0}

	def get_terms(self, equation_part, isRight):
		terms_len = 0
		for i in range(0, 3):
			matches = re.finditer(r'(?P<val>[+-]?\d+(\.)?(?(2)\d+))\*X\^' + re.escape(str(i)), equation_part)
			for match in matches:
				if isRight:
					self.terms[i] -= float(match.group('val'))
				else:
					self.terms[i] += float(match.group('val'))
				terms_len += len(match.group(0))
		if terms_len != len(equation_part) or len(equation_part) == 0:
			sys.exit('Wrong format: check that you formatted the equation correctly or that degree is less than or equal to 2')

input = get_input()
equals_count = input.count('=')
if equals_count != 1:
	sys.exit('Wrong format: found {} equals sign'.format(equals_count))
equation = Equation(input)
equation.get_terms(equation.left, False)
equation.get_terms(equation.right, True)
print(equation.terms)

# Bonus :
# - floats
# - formatting error handling