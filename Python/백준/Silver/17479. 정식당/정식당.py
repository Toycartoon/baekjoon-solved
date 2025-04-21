import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
g = 0
gs = 0
s = False

w = {}
d = {}
sp = set()
for i in range(a):
    x, n = input().strip().split()
    w[x] = int(n)

for i in range(b):
    x, n = input().strip().split()
    d[x] = int(n)

for i in range(c):
    sp.add(input().strip())

f = True
for n in range(int(input())):
    x = input().strip()

    if x in w:
        g += w[x]
    if x in d:
        gs += d[x]
    if x in sp:
        if s:
            f = False
            break
        s = True

if g < 20000 and gs != 0:
    f = False

if g + gs < 50000 and s:
    f = False

if f:
    print("Okay")
else:
    print("No")
