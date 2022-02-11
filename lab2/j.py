n = int(input())
b = []
ctr = 0
for i in range(n):
    b.append(input())

sett = set(b)
a = list(sett)
size_list_set = len(a)

for i in range(len(a)):
    if any(map(str.isupper, a[i])) and any(map(str.islower, a[i])) and any(map(str.isdigit, a[i])):
        ctr += 1
        a.append(a[i])

del a[:size_list_set]
a.sort()
print(ctr)
for i in range(ctr):
    print(a[i])