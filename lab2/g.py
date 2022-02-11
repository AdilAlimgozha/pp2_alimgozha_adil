n = int(input())
dem = [input().split() for i in range(n)]
m = int(input())
dhun = [input().split() for i in range(m)]

d = {}
for i in range(m):
    if dhun[i][1] not in d:
        d[dhun[i][1]] = int(dhun[i][2])
    else:
        d[dhun[i][1]] += int(dhun[i][2])

d_list = []
for key, val in d.items():
    d_list.append([key, val])

ctr = 0
dem1 = []
for i in range(n):
    for j in range(len(d_list)):
        if d_list[j][1] != 0:
            if dem[i][1] == d_list[j][0]:
                #dem1.append(list(dem[i]))
                ctr += 1
                d_list[j][1] = d_list[j][1] - 1
                break
        else:
            continue
    
print("Demons left:", len(dem) - ctr)