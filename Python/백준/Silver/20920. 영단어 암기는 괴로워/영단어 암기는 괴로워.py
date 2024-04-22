import sys


input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for i in range(n):
    s = input().strip()
    if len(s) < m:
        continue
    if s in d:
        d[s] += 1
    else:
        d[s] = 1


a = []
for i in d.keys():
    a.append((i, d[i]))


a = sorted(sorted(sorted(a), key=lambda x: len(x[0]), reverse=True), key=lambda x: x[1], reverse=True)

for i in a:
    print(i[0])
