def rev(s):
    s1 = ""
    for i in range(len(s) - 1, - 1, -1):
        s1 = s1 + " " + s[i]
    print(s1.strip())

s = input().split()
rev(s)
#done