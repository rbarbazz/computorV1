import sys
import argparse
import re
from Equation import Equation

# When the program is called from CLI
def get_input():
	parser = argparse.ArgumentParser(description='Solve a polynomial equation up to degree 2')
	parser.add_argument('equation', help='Format: \"n * X^[0-2]\"')
	return re.sub(r'\s+', '', parser.parse_args().equation)

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
# - formatting error handling : wrong degree, wrong format