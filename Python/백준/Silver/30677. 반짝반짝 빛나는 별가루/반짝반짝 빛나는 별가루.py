import math, sys

input = sys.stdin.readline

n, k, c, r = map(int, input().split())
base = list(map(int, input().split()))
s = list(map(int, input().split()))
p = list(map(int, input().split()))

combo = 0
stardust = 0
skill = [0] * k

t = 0
for _ in range(n):
    i = int(input())
    if i == 0:
        combo = 0
        t -= r
        if t < 0:
            t = 0
    else:
        stardust += math.floor(base[i-1] * (100 + (combo * c)) * (100 + (skill[i-1] * s[i-1])) / 10000)
        combo += 1
        skill[i - 1] += 1
        t += p[i - 1]

    if t > 100:
        break


if t <= 100:
    print(stardust)
else:
    print(-1)
