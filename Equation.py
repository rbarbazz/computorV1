import re

class Equation:
	def __init__(self, input):
		self.left = input.split('=')[0]
		self.right = input.split('=')[1]
		self.terms = {term : 0 for term in range(0, 10)}

	# Check if degree is < 10
	def check_degree(self):
		return re.search(r'\^\d{2,}', self.left) == None\
		and re.search(r'\^\d{2,}', self.right) == None

	# Check if both sides are valid
	def check_terms(self):
		return self.get_term(self.left, False) and self.get_term(self.right, True)

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
		return terms_len == len(equation_part) and len(equation_part) != 0

	def get_reduced_form(self):
		reduced_form = ''
		for term, value in self.terms.items():
			if value != 0:
				reduced_form += '{}{}{} * X^{} '.format(["", "+ "][value > 0], ["", "- "][value < 0], abs(value), str(term))
		reduced_form = re.sub(r'^\+ ', '', reduced_form)
		return 'Reduced form: '\
				+ re.sub(r'\.0 ', ' ', reduced_form)\
				+ '= 0'

	def get_degree(self):
		for term, value in self.terms.items():
			if value != 0:
				self.degree = term
		return self.degree

	# b^2 - 4ac
	def get_delta(self):
		return ((self.terms[1] ** 2) - (4 * self.terms[2] * self.terms[0]))

	# def solve_equation(self):
	# 	if self.degree == 1: