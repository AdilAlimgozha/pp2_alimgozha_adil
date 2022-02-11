n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if n % 2 == 0:
            if i >= j:
                a[i][j] = '#'
        elif n % 2 != 0:
            if i + j >= (n - 1):
                a[i][j] = '#'

for i in range(n):
    for j in range(n):
        print(a[i][j], end = '')
    print()