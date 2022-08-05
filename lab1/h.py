s, t = input(), input()

for i in range(len(s)):
    if t == s[i]:
        a = i
        break

for i in range(len(s)):
    if t == s[i]:
        b = i

if a == b:
    print(a)
else:
    print(a, b)
#fsfdsd