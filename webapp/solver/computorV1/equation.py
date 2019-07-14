import re


class Equation:
    def __init__(self, input):
        self.left = input.split('=')[0]
        self.right = input.split('=')[1]
        self.terms = {term: 0 for term in range(0, 3)}
        self.degree = 0

    # Check if both sides are valid
    def check_terms(self):
        return (
            self.get_term(self.left, False) and
            self.get_term(self.right, True)
        )

    # Match a * X^N, add and sub recurring values and makes a dict {a : N}
    def get_term(self, equation_part, isRight):
        terms_len = 0
        matches = re.finditer(
            r'(?P<val>[+-]?\d+(\.)?(?(2)\d+))\*X\^(?P<pow>\d+)', equation_part
        )

        for match in matches:
            i = int(match.group('pow'))
            if i not in self.terms.keys():
                self.terms.update({i: 0})
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
                reduced_form += '{}{}{} * X^{} '.format(
                    ["", "+ "][value > 0],
                    ["", "- "][value < 0],
                    abs(value),
                    str(term)
                )
        reduced_form = re.sub(r'^\+ ', '', reduced_form)
        return (
            'Reduced form: ' +
            re.sub(r'\.0 ', ' ', reduced_form) +
            '= 0\n'
        )

    def get_degree(self):
        for term, value in self.terms.items():
            if value != 0:
                self.degree = term
        return self.degree

    def solve(self):
        a = self.terms[2]
        b = self.terms[1]
        c = self.terms[0]

        if self.degree == 1:
            solution = 'The solution is:\n' + str(-c / b)
        else:
            self.delta = b ** 2 - (4 * a * c)
            solution = 'Discriminant: ' + str(self.delta)
            if self.delta < 0:
                solution += '\nThe discriminant is stricly negative, there are two complex solution:\n'
                first_part = str(-b / (2 * a))
                sec_part = str(((-self.delta) ** 0.5) / (2 * a))
                solution += first_part + '- ' + sec_part + 'i\n'
                solution += first_part + '+ ' + sec_part + 'i'
            elif self.delta == 0:
                solution += '\nThe discriminant is null, there is one solution:\n'
                solution += str(-b / (2 * a))
            else:
                solution += '\nThe discriminant is stricly positive, there are two solutions:\n'
                solution += str((-b - self.delta ** 0.5) / (2 * a)) + '\n'
                solution += str((-b + self.delta ** 0.5) / (2 * a))

        return re.sub(r'\.0', ' ', solution)
