class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Shape):
    def area(self):
        print(self.length * self.width)

s = Rectangle(int(input()), int(input()))
s.area()
#done