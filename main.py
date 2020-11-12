from fractions import Fraction as Frac
from numpy import random as r
from numpy import lcm
from numpy import gcd

values = [x for x in range(1, 15)]


class CreateFraction:
    def __init__(self, num=None):
        if num is None:
            self.frac = self.create_fraction()
        else:
            self.frac = num
        self.tex_frac = self.frac_tex_frac(self.frac)


    @staticmethod
    def create_fraction():
        return Frac(r.choice(values), r.choice(values))


    @staticmethod
    def frac_tex_frac(frac):
        if frac.denominator == 1:
            return str(frac.numerator)
        else:
            return '\\frac{' + str(frac.numerator) + '}{' + str(frac.denominator) + '}'


class Problem:
    def __init__(self, fraction_1, fraction_2):
        self.ops_list = ['+', '-', '*', '/']
        self.operation = r.choice(self.ops_list)
        self.problem = '$' + self.create_problem(fraction_1, fraction_2) + '$'
        self.solution = '$' + self.create_solution(fraction_1, fraction_2) + '$'


    def create_problem(self, fraction_1, fraction_2):
        if self.operation == '*':
            return fraction_1.tex_frac + ' \\times ' + fraction_2.tex_frac
        elif self.operation == '/':
            return fraction_1.tex_frac + ' \\div ' + fraction_2.tex_frac
        else:
            return fraction_1.tex_frac + ' ' + self.operation + ' ' + fraction_2.tex_frac


    def create_solution(self, fraction_1, fraction_2):
        if self.operation == '+':
            solution = CreateFraction(fraction_1.frac + fraction_2.frac)
            return solution.tex_frac
        elif self.operation == '-':
            solution = CreateFraction(fraction_1.frac - fraction_2.frac)
            return solution.tex_frac
        elif self.operation == '/':
            solution = CreateFraction(fraction_1.frac / fraction_2.frac)
            return solution.tex_frac
        else:
            solution = CreateFraction(fraction_1.frac * fraction_2.frac)
            return solution.tex_frac


class TexOutputProblem:
    def __init__(self, problem):
        self.output = ['\\question ' + problem.problem + '\n',
                       '\t\\begin{solution}' + '\n',
                       2 * '\t' + problem.solution + '\n',
                       '\t\\end{solution}' + '\n\n']


class MultiplesFactorsProblems:
    def __init__(self):
        self.num_of_nums = r.randint(2, 5)
        self.nums = [r.randint(2, 20) for x in range(self.num_of_nums)]
        self.str_nums = self.convert_list_to_string()
        self.problem = self.create_problem()
        self.solutionNumerical = self.create_solution()
        self.solution = self.texify_solution()

    def convert_list_to_string(self):
        str_of_nums = ''
        for x in range(len(self.nums)):
            if x == len(self.nums) - 1:
                str_of_nums += str(self.nums[x])
            else:
                str_of_nums += str(self.nums[x]) + ', '
        return str_of_nums


    def create_solution(self):
        return [gcd.reduce(self.nums),
                lcm.reduce(self.nums)]


    def texify_solution(self):
        return 'The GCD is ' + str(self.solutionNumerical[0]) + \
                ' and the LCM is ' + str(self.solutionNumerical[1])

    def create_problem(self):
        return 'Find the GCD and LCM of ' + self.str_nums + '.\n'


# Read in head and tail for tex file
with open('head.txt', 'r') as infile:
    head = infile.read()

with open('tail.txt', 'r') as infile:
    tail = infile.read()

# Open tex file for writing
with open('WS-Fractions.tex', 'w') as of:
    # Write preamble for tex file
    of.writelines(head)

    # Number of problems to be produced.
    num_questions = 20
    q1 = MultiplesFactorsProblems()
    print(TexOutputProblem(q1))
    # Loom to create selected number of Fraction Operation questions
    # Create problems
    # Write to file
    for x in range(num_questions):
        fractions = [CreateFraction(), CreateFraction()]
        p = Problem(fractions[0], fractions[1])

        out = TexOutputProblem(p)
        of.writelines(out.output)

    # Write closing statements
    of.writelines(tail)
