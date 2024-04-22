from math import gcd
import sys

input = sys.stdin.readline

p = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

a = 0
m = set()
for i in range(n):
    x, y = p[i]
    g = gcd(x, y)
    if (x // g, y // g) not in m:
        a += 1
        m.add((x // g, y // g))


print(a)