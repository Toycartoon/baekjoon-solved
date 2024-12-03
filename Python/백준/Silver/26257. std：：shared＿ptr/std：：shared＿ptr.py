import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())

p = [int(input()) for _ in range(m)]
for i in range(q):
    com, x, *y = input().split()

    if com == "assign":
        p[int(x)-1] = p[int(y[0])-1]
    elif com == "swap":
        p[int(x)-1], p[int(y[0])-1] = p[int(y[0])-1], p[int(x)-1]
    elif com == "reset":
        p[int(x)-1] = 0

ans = []
for i in set(p):
    if i != 0:
        ans.append(i)

print(len(ans))
for i in sorted(ans):
    print(i)
