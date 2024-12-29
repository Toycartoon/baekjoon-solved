import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append(b - a)


l.sort()
print(l[k-1] if l[k-1] >= 0 else 0)
