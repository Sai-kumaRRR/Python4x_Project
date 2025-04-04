# method overloading



class MathUtils:
   # Method- overloading - Not

    # supported!

 def add(self, a=10, b=20):
    return a + b


def add(self, a=4, b=8, c=6):
    return a + b + c


def add(self, a=0, b=0, c=0, d=0):
    return a + b + c + d


math = MathUtils()
op1 = math.add(1, 2)
op1 = math.add(1, 2, 26)
op1 = math.add(1, 2, 45, 32)
