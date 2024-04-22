import sys

n, s = input().split()
d = set()
p = 0
np = 0
a = 0
if s == "Y":
    np = 1
elif s == "F":
    np = 2
else:
    np = 3

for _ in range(int(n)):
    h = sys.stdin.readline()
    if h not in d:
        p += 1
        d.add(h)

    if p == np:
        a += 1
        p = 0

print(a)