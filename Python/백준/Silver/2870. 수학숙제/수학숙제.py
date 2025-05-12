import re

n = int(input())
ans = []
for i in range(n):
    ans.extend([*map(int, re.findall(r"\d+", input()))])

ans.sort()
for i in ans:
    print(i)
