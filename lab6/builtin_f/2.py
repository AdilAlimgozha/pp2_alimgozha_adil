s = input()
ctrup, ctrdown = 0, 0
for x in s:
    if x.isupper():
        ctrup += 1 
    elif x.islower():
        ctrdown += 1

x = "print('upper', ctrup)"
y = "print('lower', ctrdown)"
exec(x)
exec(y)
#done