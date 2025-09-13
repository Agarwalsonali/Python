import math

class Calculator:
    def square(self,n):
        self.n = n
        print(f"Square of {n} is {n*n}")

    def cube(self,n):
        self.n = n
        print(f"Cube of {n} is {n*n*n}")
    
    def square_root(self,n):
        self.n = n
        print(f"Square Root of {n} is {math.sqrt(n)}")

number = Calculator()
number.square(5)
number.cube(2)
number.square_root(16)

        