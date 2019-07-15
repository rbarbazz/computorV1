import argparse
import re
import sys
from .equation import Equation


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
