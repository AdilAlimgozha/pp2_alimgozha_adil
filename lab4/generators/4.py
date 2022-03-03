def squares():
    a, b = int(input()), int(input())
    while a <= b:
        yield a**2
        a += 1
sqr = squares()
for i in sqr:
    print(i, end = ' ')
#done