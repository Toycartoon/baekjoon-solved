import sys

input = sys.stdin.readline

tm = {}
mt = {}
n, m = map(int, input().split())

for i in range(n):
    t = input().strip()
    x = []
    for j in range(int(input())):
        mem = input().strip()
        mt[mem] = t
        x.append(mem)

    tm[t] = x


for i in range(m):
    x = input().strip()
    q = int(input())

    if q == 0:
        [print(i) for i in sorted(tm[x])]
    elif q == 1:
        print(mt[x])
