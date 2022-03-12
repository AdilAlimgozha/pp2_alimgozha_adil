import re

txt = input()
x = re.search(".*a.+b$", txt)

if x:
    print(x)
    print("Matches")
else:
    print("NO")
#done