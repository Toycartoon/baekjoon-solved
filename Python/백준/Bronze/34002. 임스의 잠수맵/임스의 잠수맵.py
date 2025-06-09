from math import ceil

a, b, c = map(int, input().split())
s, v = map(int, input().split())
l = int(input())

exp = (250 - l) * 100

if c * v * 30 >= exp:
    print(ceil(exp / c))
    exit()

exp -= c * v * 30
if b * s * 30 >= exp:
    print(v * 30 + ceil(exp / b))
    exit()

exp -= b * s * 30
print(ceil(exp / a) + s * 30 + v * 30)
