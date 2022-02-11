n = int(input())
a = [0]*n
for i in range(n):
    a[i] = [0]*n
    for j in range(n):
        if i == 0:
            a[i][j] = j
        elif j == 0:
            a[i][j] = i
        elif i == j:
            a[i][j] = i*j

for i in range(n):
    for j in range(n):
        print(a[i][j], end = " ")
    print()