class Calculation1:
    def add(self, a, b):
        return a+b

class Calculation2:
    def subtract(self, a, b):
        return a-b

class Calculation3:
    def multiply(self, a, b):
        return a*b


class Calculation(Calculation1, Calculation2, Calculation3):
    def divide(self, a, b):
         return a/b

c = Calculation()
print(c.subtract(56, 6))
print(c.add(30, 8))
print(c.multiply(4, 3))