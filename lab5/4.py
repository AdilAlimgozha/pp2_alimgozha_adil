import re

txt = input()
x = re.findall("[a-z]([A-Z])", txt)
print(x)
#done