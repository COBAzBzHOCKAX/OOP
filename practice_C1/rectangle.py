import math

class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
       	self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.width == other.height and self.width == other.height

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}'

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2

    def __eq__(self, other):
        return self.a == other.a


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return math.pi * (self.r ** 2)