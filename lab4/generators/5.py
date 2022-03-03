def down():
    n = int(input())
    while n >= 0:
        yield n
        n -= 1

Down = down()
for i in Down:
    print(i, end = ' ')
#done