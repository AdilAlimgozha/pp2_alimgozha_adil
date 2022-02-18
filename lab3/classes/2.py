class Shape:
    def area(self):
        print(self.length ** 2)

class Square(Shape):
    def __init__(self, length):
        self.length = length

S = Square(int(input()))
S.area()
#done