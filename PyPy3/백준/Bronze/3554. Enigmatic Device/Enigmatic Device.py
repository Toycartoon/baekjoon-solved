import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

for q in range(int(input())):
    k, l, r = map(int, input().split())

    if k == 1:
        for i in range(l-1, r):
            a[i] **= 2
            a[i] %= 2010
    elif k == 2:
        x = 0
        for i in range(l-1, r):
            x += a[i]
        print(x)
