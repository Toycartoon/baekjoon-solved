from math import sin

a, b, c = map(int, input().split())

l, r = -1, 100001
x = (l + r) / 2

for i in range(100):
    x = (l + r) / 2

    if a * x + b * sin(x) == c:
        break
    elif a * x + b * sin(x) < c:
        l = x
    else:
        r = x


print(x)
