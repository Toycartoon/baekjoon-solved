import sys

input = sys.stdin.readline

b, n, m = map(int, input().split())
w = {}
for t in range(n):
    i, p = input().strip().split()
    w[i] = int(p)

ans = 0
for x in range(m):
    j = input().strip()
    ans += w[j]

if b >= ans:
    print("acceptable")
else:
    print("unacceptable")
