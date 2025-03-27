import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = []
for i in range(n):
    t.append(int(input()))

l, r = 0, max(t)*m+1
while l + 1 < r:
    mid = (l + r) // 2
    
    x = 0
    for i in t:
        x += mid // i
    
    if x >= m:
        r = mid

    else:
        l = mid

print(r)