import sys

input = sys.stdin.readline

n = int(input())
w = {}
for i in range(n):
    k, m = input().strip().split()

    if k not in w:
        w[k] = int(m)
    else:
        w[k] += int(m)


for i in sorted(w.keys()):
    print(i, w[i])
