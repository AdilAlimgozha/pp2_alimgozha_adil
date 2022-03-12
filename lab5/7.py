import re

txt = input()
x = re.split("_", txt)

for i in range(len(x)):
    x[i] = x[i].capitalize()

print("".join(x))
#done