import sys

input = sys.stdin.readline

n = int(input())
s = []
w = {}
for i in range(n):
    x = input().split()
    s.append(x)

    for v in x:
        w[v] = i


l = input().split()

f = True
idx = [0 for _ in range(n)]

for i in l:
    if i not in w:
        f = False
        break

    if s[w[i]][idx[w[i]]] == i:
        idx[w[i]] += 1

        if idx[w[i]] == len(s[w[i]]):
            idx[w[i]] = 0
    else:
        f = False
        break


if f and idx.count(0) == n:
    print("Possible")
else:
    print("Impossible")
