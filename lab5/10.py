import re

txt = input()
x = re.findall("[A-Z][^A-Z]*", txt)
for i in range(len(x)):
    x[i] = x[i].lower()

print("_".join(x))
#done