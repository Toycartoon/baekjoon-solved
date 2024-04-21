import sys


input = sys.stdin.readline

n = int(input())
x1, y1 = map(int, input().split())
l = [(x1, y1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    l.append((x, y))

l.append((x1, y1))


s = 0
for i in range(n):
    s += l[i][0] * l[i+1][1]

for i in range(n):
    s -= l[i][1] * l[i+1][0]

print("%.1f" % (abs(s * 0.5)))
