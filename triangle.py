import math
class triangle(object):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)


    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = (self.a + self.b + self.c) / 2
        square = math.sqrt(s * ((s - self.a) * (s - self.b) * (s - self.c)))
        return square



a = input("Enter the value of a = ")
b = input("Enter the value of b = ")
c = input("Enter the value of c = ")

t = triangle(a, b, c)
print(t.perimeter())
print(t.square())