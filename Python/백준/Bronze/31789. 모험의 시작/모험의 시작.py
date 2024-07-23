import sys

input = sys.stdin.readline

n = int(input())
x, s = map(int, input().split())

f = False
for i in range(n):
    c, p = map(int, input().split())
    if c <= x and p > s:
        f = True
        break

if f:
    print("YES")
else:
    print("NO")
