import sys

input = sys.stdin.readline

n, s = input().split()
ans = 0
for _ in range(int(n)):
    name, c = input().split()
    for i in name.split("_"):
        if i == s:
            ans += int(c)
            break

print(ans)