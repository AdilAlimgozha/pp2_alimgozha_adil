s = input()
a = []
flag = True
for i in range(len(s)):
    if s[i] == '(' or s[i] == '[' or s[i] == '{':
        a.append(s[i])
    elif len(a) != 0 and ((s[i] == ')' and a[-1] == '(') or (s[i] == ']' and a[-1] == '[') or (s[i] == '}' and a[-1] == '{')):
        a.pop()
    else:
        flag = False
if (len(a) == 0 and flag == True):
    print('Yes')
else:
    print('No')