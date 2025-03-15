from math import ceil

n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    n -= ceil(i / 2)

if n <= 0:
    print("YES")
else:
    print("NO")
