import sys

input = sys.stdin.readline

a = []
n = int(input())
for i in range(n):
    a.append(int(input()))

a.sort()
ans = []
for i in range(n):
    ans.append(a[i] * (n - i))

print(max(ans))
