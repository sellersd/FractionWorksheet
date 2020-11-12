from fractions import Fraction as f
from numpy import random as r

values = [x for x in range(1, 15)]

class fraction:
    def __init__(self, num = None):
        if num == None:
           self.frac = self.create_fraction()
        else:
            self.frac = num
        self.tex_frac = self.frac_tex_frac(self.frac)


    def create_fraction(self):
        return f(r.choice(values), r.choice(values))


    def frac_tex_frac(self, frac):
        if frac.denominator == 1:
            return str(frac.numerator)
        else:
            return '\\frac{' + str(frac.numerator) + '}{' + str(frac.denominator) + '}'


class Problem:
    def __init__(self, frac1, frac2):
        self.ops_list = ['+', '-', '*', '/']
        self.operation = r.choice(self.ops_list)
        self.problem = '$' + self.create_problem(frac1.tex_frac, frac2.tex_frac) + '$'
        self.solution = '$' + self.create_solution(frac1, frac2) + '$'

    def create_problem(self, frac_obj1, frac_obj2):
        if self.operation == '*':
            return frac1.tex_frac + ' \\times ' + frac2.tex_frac
        elif self.operation == '/':
            return frac1.tex_frac + ' \\div ' + frac2.tex_frac
        else:
            return frac1.tex_frac + ' ' + self.operation + ' ' + frac2.tex_frac

    def create_solution(self, frac1, frac2):
        if self.operation == '+':
           soln = fraction(frac1.frac + frac2.frac)
           return soln.tex_frac
        elif self.operation == '-':
            soln = fraction(frac1.frac - frac2.frac)
            return soln.tex_frac
        elif self.operation == '/':
            soln = fraction(frac1.frac / frac2.frac)
            return soln.tex_frac
        else:
            soln = fraction(frac1.frac * frac2.frac)
            return soln.tex_frac


class TexOutputProblem:
    def __init__(self, problem):
        self.output = ['\\question ' + problem.problem + '\n',
                       '\t\\begin{solution}' + '\n',
                       2*'\t' + problem.solution + '\n',
                       '\t\\end{solution}' + '\n\n']


with open('head.txt', 'r') as infile:
    head = infile.read()

with open('tail.txt', 'r') as infile:
    tail = infile.read()

with open('WS-Fractions.tex', 'w') as of:
    of.writelines(head)
    num_questions = 20
    for x in range(num_questions):
        frac1 = fraction()
        frac2 = fraction()
        p = Problem(frac1, frac2)
        # print(p.problem)
        # print(p.solution)

        out = TexOutputProblem(p)
        of.writelines(out.output)
    of.writelines(tail)
