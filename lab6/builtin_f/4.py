import time

n, milsec = int(input()), int(input())
time.sleep(milsec/1000)
sqrt_n = pow(n, 0.5)

print("Square root of", n, "after", milsec, "miliseconds is", sqrt_n)
#done