import sys


input = sys.stdin.readline

n, m, q = map(int, input().split())

l = []
for i in range(n):
    l.append(list(map(int, input().split())))


for _ in range(q):
    com, i, j, *k = map(int, input().split())

    if com == 0:
        l[i][j] = k[0]
    elif com == 1:
        l[i], l[j] = l[j], l[i]


for x in l:
    print(*x)
