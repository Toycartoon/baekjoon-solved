from collections import deque


n = int(input())
t = int(input())
a = deque(map(int, input().split()))
b = list(map(int, input().split()))

for x in b:
    for i in range(x-1):
        a.rotate(-1)

    print(a[0], end=" ")
