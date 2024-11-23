import sys

input = sys.stdin.readline

n, m = map(int, input().split())
f = True
for i in range(m):
    k = int(input())
    l = list(map(int, input().split()))
    
    for i in range(1, k):
        if l[i] > l[i-1]:
            f = False
            break

if f:
    print("Yes")
else:
    print("No")