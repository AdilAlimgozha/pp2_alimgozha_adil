def filter_prime(n, i):
    if i == 0:
        return
    if i == 1:
        a_prime.append(n)
    else:
        if n % i != 0:
            return filter_prime(n, i - 1)
        else:
            return

a = list(map(int, input().split()))
a_prime = []
for i in range(len(a)):
    filter_prime(a[i], a[i] - 1)
print(a_prime)
#done