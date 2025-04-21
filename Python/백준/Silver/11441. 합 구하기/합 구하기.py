import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ps = []
x = 0
for i in a:
    ps.append(x)
    x += i

ps.append(x)
for m in range(int(input())):
    i, j = map(int, input().split())
    print(ps[j]-ps[i-1])
