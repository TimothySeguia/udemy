import math


# Object Oriented Programming examples
class Shape:
    def what_am_i(self):
        return "I am a shape!"


class Rectangle(Shape):
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Shape):
    def __init__(self,l):
        self.length = l

    def change_size(self, n):
        self.length += n

    def calculate_perimeter(self):
        return self.length * 4


a_rectangle = Rectangle(4,4)
a_square = Square(4)
print("%d rectangle perimeter" % a_rectangle.calculate_perimeter())
print("%d square perimeter" % a_square.calculate_perimeter())
a_square.change_size(5)
print("%d square change size" % a_square.calculate_perimeter())
print(a_rectangle.what_am_i())
print(a_square.what_am_i())


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


a_circle = Circle(4)
print(int(a_circle.area()))


# Composition example
class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r


class Rider:
    def __init__(self, n):
        self.name = n


astolfo = Rider("Astolfo")
horse = Horse("Griffin", astolfo)
print(horse.rider.name)
astolfo.name = "help"
print(horse.rider.name)
