import sys

input = sys.stdin.readline

n, s = map(int, input().split())
l = []

for i in range(n):
    l.append(int(input()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue

        if l[i] + l[j] <= s:
            ans += 1

print(ans)
