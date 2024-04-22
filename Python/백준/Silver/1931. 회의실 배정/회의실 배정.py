import sys

a = 0
l = []
for _ in range(int(input())):
    s, e = map(int, sys.stdin.readline().split())
    l.append((s, e))

l = sorted(sorted(l, key=lambda x: x[0]), key=lambda y: y[1])
a = 0
de = 0
for i in l:
    if de <= i[0]:
        de = i[1]
        a += 1

print(a)