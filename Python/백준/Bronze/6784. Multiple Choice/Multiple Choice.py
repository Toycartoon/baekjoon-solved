import sys

input = sys.stdin.readline

a = []
n = int(input())
for i in range(n):
    a.append(input().strip())

ans = 0
for i in range(n):
    if a[i] == input().strip():
        ans += 1

print(ans)
