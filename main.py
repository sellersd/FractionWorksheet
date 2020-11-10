from fractions import Fraction as f
from numpy import random as r

values = [x for x in range(1, 15)]


def create_fraction():
    return f(r.choice(values), r.choice(values))


def frac_tex_frac(frac):
    if frac.denominator == 1:
        return str(frac.numerator)
    else:
        return '\\frac{' + str(frac.numerator) + '}{' + str(frac.denominator) + '}'


def addition_fraction_problem(frac1, frac2):
    return frac1 + ' + ' + frac2


def subtraction_fraction_problem(frac1, frac2):
    return frac1 + ' - ' + frac2


def multiplication_fraction_problem(frac1, frac2):
    return frac1 + ' \\times ' + frac2


def division_fraction_problem(frac1, frac2):
    return frac1 + ' \\div ' + frac2


def create_problem(frac1, frac2, problem_type)
    if frac1.denominator == 1 and frac2.denominator == 2:
        return False
    else:

with open('head.txt', 'r') as infile:
    head = infile.read()

with open('tail.txt', 'r') as infile:
    tail = infile.read()

with open('WS-Fractions.tex', 'w') as of:
    of.writelines(head)

    for x in range(20):
        of.write(addition_fraction_problem(frac_tex_frac(create_fraction()), frac_tex_frac(create_fraction())) + '\n')
        of.write(
            subtraction_fraction_problem(frac_tex_frac(create_fraction()), frac_tex_frac(create_fraction())) + '\n')
        of.write(
            multiplication_fraction_problem(frac_tex_frac(create_fraction()), frac_tex_frac(create_fraction())) + '\n')
        of.write(division_fraction_problem(frac_tex_frac(create_fraction()), frac_tex_frac(create_fraction())) + '\n')
        of.write('\n')
    of.writelines(tail)
