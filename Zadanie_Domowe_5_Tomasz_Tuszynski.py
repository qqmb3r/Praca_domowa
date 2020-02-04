import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, a, b, c):
        self.set_params(a, b, c)

    def set_params(self, a, b,c):
        self._a = a
        self._b = b
        self._c = c

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b
    def get_c(self):
        return self._c

    def __str__(self):
        return "{0}: [{1},{2},{3}]".format(self.__class__.__name__, self._a, self._b, self._c)

    @abstractmethod
    def calc_surface(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b, 0)
    def calc_surface(self):
        return self._a*self._b
        #return self.get_a()*self.get_b()

class Circle(Shape):
    def __init__(self, a):
        #self.set_params(a, 0)
        super().__init__(a, 0, 0)

    def calc_surface(self):
        return math.pi*self._a**2

    def __str__(self):
        return "{0}: [{1}]".format(self.__class__.__name__, self._a)

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

class Triangle(Shape):
    def calc_surface(self):
        if (self._a + self._b) < self._c:
            return "Nie zachowano warunku trójkąta!"

        elif (self._a + self._c) < self._b:
            return "Nie zachowano warunku trójkąta!"

        elif (self._b + self._c) < self._a:
            return "Nie zachowano warunku trójkąta!"

        else:
            s = 0
            s = (self._a + self._b + self._c) / 2
            return (s * (s - self._a) * (s - self._b) * (s - self._c)) ** 0.5

class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


s = Rectangle(4, 5)
#s = Shape(4, 5)


print(s)
print(s.calc_surface())
c = Circle(5)
print(c)
print(c.calc_surface())

sq = Square(4)
print(sq)
print(sq.calc_surface())

tr = Triangle(4,5,5)
print(tr)
print(tr.calc_surface())

tr_error = Triangle(4,5,15)
print(tr_error)
print(tr_error.calc_surface())

eqTR = EquilateralTriangle(5)
print(eqTR)
print(eqTR.calc_surface())