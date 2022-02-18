class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
        self.x1 = self.x + 5
        self.y1 = self.y + 5

    def dist(self):
        import math
        print(math.sqrt((self.y1 - self.y)**2 + (self.x1 - self.x)**2))

p = Point(int(input()), int(input()))
p.show()
p.move()
p.dist()
#done