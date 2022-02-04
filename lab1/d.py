x = int(input())
z = str(input())
if z == "b":
    print(x * 1024)
else:
    c = str(input())
    print(format(x / 1024, "." + c + "f"))