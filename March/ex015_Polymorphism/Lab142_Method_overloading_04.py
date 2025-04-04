# Method overloading is not supported - Python

class Calc:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c

    Calc_ref = Calc()
    result = Calc_ref.sum(3, 4)
    print(result)
