import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

d = a[1] - a[0]
if a[1] + d == a[2]:
    print(a[-1] + d)
else:
    print(a[-1] * (a[1] // a[0]))
