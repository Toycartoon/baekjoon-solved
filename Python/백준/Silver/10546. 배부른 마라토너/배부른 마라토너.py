import sys

input = sys.stdin.readline

n = int(input())
s = set()

for i in range(n*2-1):
    x = input().strip()
    if x in s:
        s.remove(x)
    else:
        s.add(x)

print(s.pop())
