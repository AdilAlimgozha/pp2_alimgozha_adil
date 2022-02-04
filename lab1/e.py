n, f = map(int, input().split())
prime = True
for i in range(2, n):
    if (n % i) != 0:
        continue
    else:
        prime = False
        break

if n <= 500 and f % 2 == 0 and prime == True:
    print("Good job!")
else:
    print("Try next time!")