sett = set((input().split(" ")))
print(len(sett))
l = list(sett)
l.sort()
for x in l:
    if "!" in x or "," in x or "?" in x:
        print(x[:-1])
    else:
        print(x)