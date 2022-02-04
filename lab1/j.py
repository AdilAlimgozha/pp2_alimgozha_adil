s = input().split()
res = ""
for i in range(len(s)):
    if len(s[i]) >= 3:
        res = res + s[i] + " "
print(res)