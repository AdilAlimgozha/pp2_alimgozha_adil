a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

if len(a) % 2 == 0:
    for i in range(len(a) // 2):
        print(a[i] + a[len(a) - 1 - i], end = ' ')
else:
    for i in range(len(a) // 2 + 1):
        if i == len(a) - 1 - i:
            print(a[i])
        else:
            print(a[i] + a[len(a) - 1 - i], end = ' ')