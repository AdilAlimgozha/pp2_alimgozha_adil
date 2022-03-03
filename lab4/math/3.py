n, length = int(input()), int(input())
import math
P = n * length
a = length / 2 * math.tanh(360 / n / 2)
print(int(P * a / 2))
#done