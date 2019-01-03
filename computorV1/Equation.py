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
		return terms_len == len(equation_part) and len(equation_part) != 0

	def get_reduced_form(self):
		reduced_form = ''
		for term, value in self.terms.items():
			if value != 0:
				reduced_form += '{}{}{} * X^{} '.format(["", "+ "][value > 0], ["", "- "][value < 0], abs(value), str(term))
		reduced_form = re.sub(r'^\+ ', '', reduced_form)
		return 'Reduced form: '\
				+ re.sub(r'\.0 ', ' ', reduced_form)\
				+ '= 0\n'

	def get_degree(self):
		for term, value in self.terms.items():
			if value != 0:
				self.degree = term
		return self.degree

	def solve(self):
		if self.degree == 1:
			solution = 'The solution is:\n' + str(-self.terms[0] / self.terms[1])
		else:
			self.delta = self.terms[1]**2 - (4 * self.terms[2] * self.terms[0])
			solution = 'Discriminant: ' + str(self.delta)
			if self.delta < 0:
				solution += '\nThe discriminant is stricly negative, there is no solution'
			elif self.delta == 0:
				solution += '\nThe discriminant is null, there is one solution:\n'\
				+ str(-self.terms[1] / (2 * self.terms[2]))
			else:
				solution += '\nThe discriminant is stricly positive, there are two solutions:\n'\
				+ str((-self.terms[1] - self.delta**0.5) / (2 * self.terms[2])) + '\n'\
				+ str((-self.terms[1] + self.delta**0.5) / (2 * self.terms[2]))
		return solution