import sys
import argparse
import re

# When the program is called from CLI
def get_input():
	parser = argparse.ArgumentParser(description='Solve a polynomial equation up to degree 2')
	parser.add_argument('equation', help='Format: \"n * X^[0-2]\"')
	return re.sub(r'\s+', '', parser.parse_args().equation)

class Equation:
	def __init__(self, input):
		self.left = input.split('=')[0]
		self.right = input.split('=')[1]
		self.terms = {term : 0 for term in range(0, 10)}

	def check_degree(self):
		if re.search(r'\^\d{2,}', self.left)\
		or re.search(r'\^\d{2,}', self.right):
		 	return False
		return True

	def get_term(self, equation_part, isRight):
		terms_len = 0
		for i in range(0, 10):
			matches = re.finditer(r'(?P<val>[+-]?\d+(\.)?(?(2)\d+))\*X\^'\
					+ re.escape(str(i)), equation_part)
			for match in matches:
				if isRight:
					self.terms[i] -= float(match.group('val'))
				else:
					self.terms[i] += float(match.group('val'))
				terms_len += len(match.group(0))
		# Check if part is correctly formatted and not empty
		if terms_len != len(equation_part) or len(equation_part) == 0:
			return False

	def check_terms(self):
		if self.get_term(self.left, False) == False\
		or self.get_term(self.right, True) == False:
			return False
		return True

	def get_reduced_form(self):
		reduced_form = ''
		for term, value in self.terms.items():
			if value != 0:
				reduced_form += '{}{}{} * X^{} '.format(["", "+ "][value > 0], ["", "- "][value < 0],abs(value), str(term))
		reduced_form = re.sub(r'^\+ ', '', reduced_form) # Remove first + sign if exists
		return 'Reduced form: '\
				+ re.sub(r'\.0 ', ' ', reduced_form)\
				+ '= 0'

	def get_degree(self):
		for term, value in self.terms.items():
			if value != 0:
				self.degree = term
		return self.degree

if __name__ == '__main__':
	input = get_input()
	equals_count = input.count('=')
	if equals_count != 1:
		sys.exit('Wrong format: found {} equals sign'.format(equals_count))
	equation = Equation(input)
	if equation.check_degree() == False\
	or equation.check_terms() == False:
		sys.exit('Wrong format: check that you formatted the equation correctly')
	print(equation.get_reduced_form())
	print('Polynomial degree: ' + str(equation.get_degree()))
	if equation.degree > 2:
		sys.exit('The polynomial degree is stricly greater than 2, I can\'t solve.')

# Bonus :
# - floats
# - formatting error handling