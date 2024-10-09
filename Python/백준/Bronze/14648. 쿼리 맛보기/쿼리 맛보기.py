import sys

input = sys.stdin.readline

n, q = map(int, input().split())
x = list(map(int, input().split()))

for _ in range(q):
    com, a, b, *cd = map(int, input().split())

    s = 0
    if com == 1:
        for i in range(a-1, b):
            s += x[i]

        x[a-1], x[b-1] = x[b-1], x[a-1]
    else:
        for i in range(a-1, b):
            s += x[i]

        for i in range(cd[0]-1, cd[1]):
            s -= x[i]

    print(s)