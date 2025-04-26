import sys

input = sys.stdin.readline

n = int(input())
w = [0 for _ in range(50)]
for i in range(10 * n):
    for x in map(int, input().split()):
        w[x-1] += 1

f = True
for i in range(50):
    if w[i] > 2 * n:
        print(i+1, end=" ")
        f = False

if f:
    print(-1)
