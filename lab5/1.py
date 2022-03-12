import re

txt = input()
x = re.search("ab*", txt)
if x:
    print("Matches")
    print(x)
else:
    print("NO")
#done