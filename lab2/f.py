def by_value(item):
    return item[1]

n = int(input())
d = {}
for i in range(n):
    s, x = input().split()
    if s not in d:
        d[s] = int(x)
    else:
        d[s] += int(x)
        
maxvalue = 0
for j in d.values():
    if j > maxvalue:
        maxvalue = j

for i, j in d.items():
    if d[i] != maxvalue:
        d[i] = "has to receive " + str(maxvalue - j) + " tenge"
    else:
        d[i] = "is lucky!"

sor_d = sorted(d.items())
for i in range(len(sor_d)):
    print(sor_d[i][0], sor_d[i][1])