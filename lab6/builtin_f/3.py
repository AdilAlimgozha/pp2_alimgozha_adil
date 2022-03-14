s = input()
s1 = ""

for x in reversed(s):
    s1 += x

if s == s1:
    print("palindrome")
else:
    print("NO")
#done