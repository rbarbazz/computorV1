import re


def sqrt(number, number_iters=1000):
    a = float(number)
    for i in range(number_iters):
        number = 0.5 * (number + a / number)
    return number


def round_5_digit(number):
    return round(number, 5)


class Equation:
    def __init__(self, input):
        equation_parts = input.split('=')
        self.left = equation_parts[0]
        self.right = equation_parts[1]
        self.terms = {term: 0 for term in range(0, 3)}
        self.degree = 0
        self.reduced_form = ''

    # Check if both terms are valid
    def check_terms(self):
        return (
            self.get_term(self.left) and
            self.get_term(self.right, True)
        )

    # Get reduced form as a dict {exp: N}
    def get_term(self, equation_part, isRight=False):
        terms_len = 0
        reg = re.compile(
            '(?P<coef>(?:^|[-+])\d+\.\d+|(?:^|[-+])\d+)'
            '(?P<pow>\*X(?:\^(?P<exp>\d+))?)?|'
            '(?P<xpow>(?P<xsign>^|[-+])X(?P<xwpow>\^(?P<xexp>\d+))?)'
        )
        matches = re.finditer(reg, equation_part)

        for match in matches:
            # Check if the match is a * X^n or a number
            # Format: a * X
            if match.group('pow') is not None:
                coef = float(match.group('coef'))
                exp = 1
                # Format: a * X^n
                if match.group('exp') is not None:
                    exp = int(match.group('exp'))
            # Format: X
            elif match.group('xpow') is not None:
                coef = -1
                if match.group('xsign') is not '-':
                    coef = 1
                exp = 1
                # Format: X^n
                if match.group('xwpow') is not None:
                    exp = int(match.group('xexp'))
            # Format: a
            else:
                coef = float(match.group('coef'))
                exp = 0

            # Add value found to the reduced form
            if exp not in self.terms.keys():
                self.terms[exp] = 0
            if isRight:
                self.terms[exp] -= float(coef)
            else:
                self.terms[exp] += float(coef)

            terms_len += len(match.group(0))

        return terms_len == len(equation_part) and len(equation_part) != 0

    def get_reduced_form(self):
        reduced_form = ''
        rounded_terms = {
            term: round_5_digit(value) for term, value in self.terms.items()
        }
        self.terms = rounded_terms

        for term, value in self.terms.items():
            if value != 0:
                sign = '+' if value > 0 else '-'
                reduced_form += '{} {} * X^{} '.format(
                    sign,
                    abs(value),
                    term
                )
        self.reduced_form = re.sub(r'^\+ ', '', reduced_form)
        return self.reduced_form != ''

    def get_degree(self):
        for term, value in self.terms.items():
            if value != 0 and term > self.degree:
                self.degree = term
        return self.degree

    def solve(self):
        a = self.terms[2]
        b = self.terms[1]
        c = self.terms[0]

        if self.degree == 1:
            return 'The solution is:\n{} '.format(
                round_5_digit(-c / b)
            )
        else:
            self.delta = (b * b) - (4 * a * c)
            self.delta = round_5_digit(self.delta)
            solution_str = 'Discriminant: {} \n'.format(self.delta)

            if self.delta < 0:
                first_part = -b / (2 * a)
                first_part = round_5_digit(first_part)
                second_part = sqrt(-self.delta) / (2 * a)
                second_part = round_5_digit(second_part)
                solution_str += (
                    'The discriminant is stricly negative, ' +
                    'there are two complex solution:\n' +
                    '{} + i * {} \n' +
                    '{} - i * {} '
                ).format(
                    first_part,
                    second_part,
                    first_part,
                    second_part
                )
            elif self.delta == 0:
                solution_str += (
                    'The discriminant is null, ' +
                    'there is one solution:\n'
                )
                solution_str += '{} '.format(
                    round_5_digit(-b / (2 * a))
                )
            else:
                solution_str += (
                    'The discriminant is stricly positive, ' +
                    'there are two solutions:\n'
                )
                solution_str += '{} \n{} '.format(
                    round_5_digit((-b - sqrt(self.delta)) / (2 * a)),
                    round_5_digit((-b + sqrt(self.delta)) / (2 * a))
                )

        return solution_str
