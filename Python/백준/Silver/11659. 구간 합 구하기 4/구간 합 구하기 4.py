import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
ps = []

t = 0
for i in l:
    t += i
    ps.append(t)

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        sys.stdout.write(str(ps[j-1]) + "\n")
    else:
        sys.stdout.write(str(ps[j-1] - ps[i-2]) + "\n")