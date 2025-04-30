import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))
c.reverse()

l = []
for i in range(n):
    if not a[i]:
        l.append(b[i])

c.extend(l)
c.reverse()
print(*c[:m])
