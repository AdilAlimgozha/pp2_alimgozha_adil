import re

txt = input()
x = re.search("ab{3}|ab{2}", txt)
if x:
    print("Matches")
    print(x)
else:
    print("NO")
#done