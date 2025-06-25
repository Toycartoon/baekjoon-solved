import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(1, n+1):
    print(a.index(i)+1)
