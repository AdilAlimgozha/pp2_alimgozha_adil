f = open("lab6/files/copy_from.txt", "r")
f1 = open("lab6/files/copy_to.txt", "w")
for x in f:
    f1.write(x)
f.close()
f1.close()
#done