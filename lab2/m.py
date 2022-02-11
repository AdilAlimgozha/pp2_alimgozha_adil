a = []
while  True:
    b = list(input().split())
    if b[0] == "0":
        break
    a.append(b)

for i in range(len(a)):
    a[i].reverse()

a.sort()

for i in range(len(a)):
    a[i].reverse()

for i in range(len(a)):
    for j in range(3):
        print(a[i][j], end = ' ')
    print()