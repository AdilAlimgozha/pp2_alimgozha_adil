def unique():
    a = input().split()
    a_un = []
    for x in a:
        if x not in a_un:
            a_un.append(x)
    print(a_un)

unique()
#done