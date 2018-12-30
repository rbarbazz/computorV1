import sys
import argparse
import re
from Equation import Equation

# When the program is called from CLI
def get_input():
	parser = argparse.ArgumentParser(description='Solve a polynomial equation up to degree 2')
	parser.add_argument('equation', help='Format: \"n * X^[0-2]\"')
	return re.sub(r'\s+', '', parser.parse_args().equation)

def error_handler(err_code, equals_count=0):
	err = [
			'Wrong format: found {} equals sign'.format(equals_count),
			'Wrong format: check that you formatted the equation correctly',
			'Reduced form: 0 * X^0 = 0 * X^0\nPolynomial degree: 0\nAll real numbers are solution',
			'The polynomial degree is stricly greater than 2, I can\'t solve.',
			'Equation is invalid'
		]
	return err[err_code]

def computor(input):
	solution = ''
	equals_count = input.count('=')
	if equals_count != 1:
		return solution + error_handler(0, equals_count)
	equation = Equation(input)
	if not equation.check_degree() or not equation.check_terms():
		return solution + error_handler(1)
	if equation.get_reduced_form() == 'Reduced form: = 0':
		return solution + error_handler(2)
	solution += equation.get_reduced_form()
	solution += ('Polynomial degree: ' + str(equation.get_degree()) + '\n')
	if equation.degree > 2:
		return solution + error_handler(3)
	elif equation.degree == 0:
		return solution + error_handler(4)
	return solution + equation.solve()

if __name__ == '__main__':
	input = get_input()
	print(computor(input))

# Bonus :
# - floats
# - formatting error handling : wrong degree, wrong format