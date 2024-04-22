import math
import sys

input = sys.stdin.readline

a = []
x = []
t = 0
for i in range(int(input())):
    b = int(input())

    x.append(b)
    if t == 0:
        t = b
        continue
    a.append(b - t)
    t = b

g = math.gcd(*a)
print((x[-1] - x[0]) // g - len(x) + 1)
