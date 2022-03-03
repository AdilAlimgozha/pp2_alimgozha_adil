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
            if x % 3 == 0 and x % 4 == 0:
                return x
        else:
            raise StopIteration

num = Num(int(input()))
it = iter(num)
for i in it:
    if i != None:
        print(i, end = ' ')
#done