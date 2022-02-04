def b_to_d(s, i):
    if i == len(s) - 1:
        return (int(s[len(s)-1]) * 2**(len(s) - 1))
    else:
        return (int(s[i]) * 2**i) + b_to_d(s, i + 1)

s = input() [::-1]
i = 0
print(b_to_d(s, i))