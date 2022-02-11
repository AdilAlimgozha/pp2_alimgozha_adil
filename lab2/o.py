def convert_again(digit):
    d = {'0': 'ZER', '1': 'ONE', '2': 'TWO', '3': 'THR', '4': 'FOU', '5': 'FIV', '6': 'SIX', '7': 'SEV', '8': 'EIG', '9': 'NIN'}
    return d[digit]


def convert_to_triplet(n):
    s = ''
    for i in str(n):
        s = s + convert_again(i)
    return s


def convert_to_num(s):
    d = {'ZER': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOU': 4, 'FIV': 5, 'SIX': 6, 'SEV': 7, 'EIG': 8, 'NIN': 9}
    return d[s]


def plus(a, b):
    power_a, power_b = len(a) // 3, len(b) // 3
    new_a, new_b = 0, 0
    for i in range(power_a - 1, -1, -1):
        new_a = new_a + convert_to_num(a[:3]) * (10 ** i)
        a = a[3:]
    for i in range(power_b - 1, -1, -1):
        new_b = new_b + convert_to_num(b[:3]) * (10 ** i)
        b = b[3:]
    return new_a + new_b


a, b = input().split('+')
print(convert_to_triplet(plus(a, b)))