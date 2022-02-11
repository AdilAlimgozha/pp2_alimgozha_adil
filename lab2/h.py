X, Y = map(int, input().split())
a = []
n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
import math
for i in range(n):
    d = math.sqrt((X - a[i][0])**2 + (Y - a[i][1])**2)
    b.append (list((d, a[i])))

b.sort()

for x in b:
    print(x[1][0], x[1][1])