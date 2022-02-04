n = int(input())
a = [0] * n
for i in range(len(a)):
    a[i] = int(input())

for i in range(n):
    if a[i] <= 10:
        print("Go to work!")
    elif 10 < a[i] <= 25:
        print("You are weak")
    elif 25 < a[i] <= 45:
        print("Okay, fine")
    elif 45 < a[i]:
        print("Burn! Burn! Burn Young!")