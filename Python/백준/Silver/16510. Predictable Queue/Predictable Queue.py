import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))
ps = []

x = 0
for i in t:
    x += i
    ps.append(x)


for i in range(m):
    l, r = -1, n

    a = int(input())
    while l + 1 < r:
        mid = (l + r) // 2

        if ps[mid] <= a:
            l = mid
        else:
            r = mid

    print(l + 1)
