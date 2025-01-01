import sys

input = sys.stdin.readline

n, m = map(int, input().split())


ans = 0
for i in range(n):
    s, e = map(int, input().split())


for j in range(m):
    t, p = map(int, input().split())
    ans += p


print(ans / n)
