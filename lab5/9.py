import re

txt = input()
y = ""
x = re.findall("[A-Z][^A-Z]*", txt)
for i in x:
    y = y + " " + i
print(y.strip())
#done