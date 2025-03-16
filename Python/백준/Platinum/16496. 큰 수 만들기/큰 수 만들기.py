import sys
from math import lcm

input = sys.stdin.readline

n = map(int, input().split())
l = list(input().strip().split())
a = set()

for i in l:
    a.add(len(i))

c = lcm(*a)
l = sorted(l, key=lambda x: (c * x), reverse=True)

ans = ""
for i in l:
    ans += i

print(int(ans))
