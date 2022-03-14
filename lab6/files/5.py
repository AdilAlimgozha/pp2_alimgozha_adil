f = open("lab6/files/123.txt", "w")
a = []
for i  in range(4):
    a.append(input())
for x in a:
    f.write(x)
f.close()
#done