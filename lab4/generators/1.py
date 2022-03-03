#first way
n = int(input())
it = (i**2 for i in range(n))

for i in it:
    if i <= n:
        print(i)
#done


#second way
'''class Numbers():                
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        x = (self.a)**2
        if x <= self.n:
            self.a += 1
            return x
        else:
            raise StopIteration

num_class = Numbers(int(input()))
iterator = iter(num_class)

for x in iterator:
    print(x)'''