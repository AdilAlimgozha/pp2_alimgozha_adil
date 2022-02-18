def spy_game(a):
    flag = False
    for i in range(len(a) - 2):
        if a[i] == 0 and a[i + 1] == 0 and a[i + 2] == 7:
            flag = True
            break
    if flag == True:
        print(True)
    else:
        print(False)

a = list(map(int, input().split()))
spy_game(a)
#done
