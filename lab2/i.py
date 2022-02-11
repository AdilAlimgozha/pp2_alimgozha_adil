n = int(input())
b = []
c = []
for i in range(n):
    a = input().split()
    if len(a) == 2:
        b.append(a[1])
    elif len(a) == 1:
        c.append(b[0])
        b.pop(0)
for x in c:
    print(x, end = " ")
