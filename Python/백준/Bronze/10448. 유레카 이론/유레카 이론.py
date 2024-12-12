import sys
from itertools import combinations_with_replacement as h

input = sys.stdin.readline

l = []
x = 0
for i in range(1, 100):
    x += i

    if x > 1000:
        break
    l.append(x)

p = list(h(l, 3))
for t in range(int(input())):
    n = int(input())

    f = False
    for i in p:
        if sum(i) == n:
            f = True
            break

    print(int(f))
