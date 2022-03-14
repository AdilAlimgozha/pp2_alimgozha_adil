f = open("lab6/files/student_info.txt", "r")
ctr = 0
for x in f:
    ctr += 1
print(ctr, "lines")
f.close()
#done