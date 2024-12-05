import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0

f = []
for i in range(n):
    a = []

    p = int(input())
    l = list(map(int, input().split()))

    for j in range(0, p * 2, 2):
        x, y = l[j], l[j + 1]
        a.append(x ** 2 + y ** 2)

    f.append(max(a))

f.sort()
print("%.02f" % f[k-1])
