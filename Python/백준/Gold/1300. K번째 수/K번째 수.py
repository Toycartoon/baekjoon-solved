import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

l, r = 1, k
while l <= r:
    mid = (l + r) // 2

    s = 0
    for i in range(1, n + 1):
        s += min(n, mid // i)

    if s >= k:
        r = mid - 1
    else:
        l = mid + 1

print(l)
