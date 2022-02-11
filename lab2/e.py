s = input().split()
if len(s) == 1:
    s.append(input())
xor = 0
a = [0] * int(s[0])
for i in range(int(s[0])):
    a[i] = int(s[1]) + 2 * i
    xor ^= a[i]
print(xor)