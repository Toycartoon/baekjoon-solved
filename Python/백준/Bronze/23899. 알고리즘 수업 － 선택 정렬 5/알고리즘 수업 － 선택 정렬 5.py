import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


for x in range(n-1, 0, -1):
    if a == b:
        break

    t = max(a[:x+1])
    if a[x] < t:
        a[a.index(t)], a[x] = a[x], a[a.index(t)]

print(1 if a == b else 0)
