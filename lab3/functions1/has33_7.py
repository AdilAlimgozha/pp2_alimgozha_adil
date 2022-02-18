def has_33(a):
    flag = False
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] == 3:
            flag = True
            break
    if flag == True:
        print(True)
    else:
        print(False)

a = list(map(int, input().split()))
has_33(a)
#done