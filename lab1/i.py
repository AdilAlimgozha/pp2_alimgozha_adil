n = int(input())
a = [0] * n
for i in range(n):
    a[i] = input()

for i in range(n):
    if "@gmail.com" in a[i]:
        s = a[i]
        print(s[:-10])