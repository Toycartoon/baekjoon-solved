import sys

input = sys.stdin.readline

n, m = map(int, input().split())
p1, p2 = 0, 0
g = 0
for _ in range(n):
    x, y = map(int, input().split())

for _ in range(m):
    v, w, c = input().split()
    
    if c == "R":
        p1 += 1
    elif c == "B":
        p2 += 1
    else:
        if g % 2 == 0:
            p1 += 1
        else:
            p2 += 1
        g += 1

if p1 > p2:
    print("jhnah917")
else:
    print("jhnan917")
