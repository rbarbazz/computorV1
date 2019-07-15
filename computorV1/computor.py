import argparse
import re
import sys
from equation import Equation


# When the program is called from CLI
def get_input():
    parser = argparse.ArgumentParser(
        description='Solve a polynomial equation up to degree 2'
    )
    parser.add_argument('equation', help='Format: \"n * X^[0-2]\"')
    return parser.parse_args().equation


def solve_equ(input):
    solution = ''
    input = re.sub(r'\s+', '', input)

    # Check the count of equal sign
    equals_count = input.count('=')
    if equals_count != 1:
        return 'Wrong format: found {} equal signs'.format(equals_count)

    # Simplify both terms of the equation
    equation = Equation(input)
    if not equation.check_terms():
        return 'Wrong format: check that you properly formatted the equation'
    if not equation.get_reduced_form():
        return (
            'Reduced form: 0 * X^0 = 0\n' +
            'Polynomial degree: 0\n' +
            'All real numbers are solution'
        )

    solution += 'Reduced form: {}= 0\n'.format(equation.reduced_form)
    solution += 'Polynomial degree: {}\n'.format(equation.get_degree())
    if equation.degree > 2:
        return (
            solution +
            'The polynomial degree is stricly greater than 2' +
            ', sorry I can\'t solve it.'
        )
    elif equation.degree == 0:
        return solution + 'Equation is invalid'

    solution += equation.solve()
    return re.sub(r'\.0 ', ' ', solution)


if __name__ == '__main__':
    input = get_input()
    print(solve_equ(input))

# Bonus :
# - natural form inputs: a * X^n, a * X, X^n, a
# - formatting error handling : wrong degree, wrong format
# - webapp


# Todo:
# - recode sqrt
# - complex solutions
