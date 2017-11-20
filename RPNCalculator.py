from RegexDispatcher import *
import math

class RPNCalculator(RegexDispatcher):
    def __init__(self):
        RegexDispatcher.__init__(self)
        self.stack = []

    def __str__(self):
        return str(self.stack)

    # Make RPNCalculator objects callable
    def __call__(self, expression):
        # Calculate the value of expression
        for t in expression.split():
            self.dispatch(t, token=t)
        return self.top()  # return the top of the stack

    # Stack management
    def top(self):
        return self.stack[-1] if len(self.stack) > 0 else []

    def push(self, x):
        return self.stack.append(float(x))

    def pop(self, n=1):
        return self.stack.pop() if n == 1 else [self.stack.pop() for n in range(n)]

    # Handle numbers
    def number(self, regex: r"[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?", **kwargs):
        self.stack.append(float(kwargs['token']))

    # Binary operators
    def plus(self, regex: r"\+", **kwargs):
        a, b = self.pop(2)
        self.push(b + a)

    def minus(self, regex: r"\-", **kwargs):
        a, b = self.pop(2)
        self.push(b - a)

    def multiply(self, regex: r"\*", **kwargs):
        a, b = self.pop(2)
        self.push(b * a)

    def divide(self, regex: r"\/", **kwargs):
        a, b = self.pop(2)
        self.push(b / a)

    def pow(self, regex: r"exp", **kwargs):
        a, b = self.pop(2)
        self.push(a ** b)

    def logN(self, regex: r"logN", **kwargs):
        a, b = self.pop(2)
        self.push(math.log(a,b))

    # Unary operators
    def neg(self, regex: r"neg", **kwargs):
        self.push(-self.pop())

    def sqrt(self, regex: r"sqrt", **kwargs):
        self.push(math.sqrt(self.pop()))

    def log2(self, regex: r"log2", **kwargs):
        self.push(math.log2(self.pop()))

    def log10(self, regex: r"log10", **kwargs):
        self.push(math.log10(self.pop()))

    def pi(self, regex: r"pi", **kwargs):
        self.push(math.pi)

    def e(self, regex: r"e", **kwargs):
        self.push(math.e)

    def deg(self, regex: r"deg", **kwargs):
        self.push(math.degrees(self.pop()))

    def rad(self, regex: r"rad", **kwargs):
        self.push(math.radians(self.pop()))

    # Whole stack operators
    def cls(self, regex: r"c", **kwargs):
        self.stack=[]

    def sum(self, regex: r"sum", **kwargs):
        self.stack=[math.fsum(self.stack)]


if __name__ == '__main__':
    calc = RPNCalculator()

    print(calc('2 2 exp 3 + neg'))

    print(calc('c 1 2 3 4 5 sum 2 * 2 / pi'))

    print(calc('pi 2 * deg'))

    print(calc('2 2 logN'))


