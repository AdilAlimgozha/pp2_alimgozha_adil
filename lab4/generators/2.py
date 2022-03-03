class Num():
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.i = 1
        return self
    
    def __next__(self):
        x = self.i
        if x < self.n:
            self.i += 1
            if x % 2 == 0:
                return x
        else:
            raise StopIteration

class_n = Num(int(input()))
it = iter(class_n)
for i in it:
    if i != None:
        print(i, end = ', ')
#done





'''n = int(input())
it = (i if i % 2 == 0 else ", " for i in range(n + 1))

for i in it:
    print(i, end = '')'''