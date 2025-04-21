from itertools import product as pro
import sys

input = sys.stdin.readline

p = [i for i in range(501)]
p[1] = 0
for i in range(2, len(p)):
    if not p[i]:
        continue

    for j in range(i * 2, len(p), i):
        p[j] = 0

temp = []
for i in p:
    if i:
        temp.append(i)

for t in range(int(input())):
    k = int(input())

    f = False
    for x in pro(temp, repeat=3):
        if sum(x) == k:
            print(*x)
            f = True
            break

    if not f:
        print(0)
