import sys

input = sys.stdin.readline

x = []
n, q = map(int, input().split())
v = 0
for i in range(n):
    v += int(input())
    x.append(v)

for i in range(q):
    a = int(input())
    for v in range(len(x)):
        if a < x[v]:
            print(v+1)
            break
