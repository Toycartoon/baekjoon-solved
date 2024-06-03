from math import gcd
import sys

input = sys.stdin.readline


dp = [0] * 1001
dp[1] = 3
for x in range(2, 1001):
    cnt = 0
    for y in range(1, x+1):
        if gcd(x,y) == 1:
            cnt += 2

    dp[x] = dp[x-1] + cnt


for c in range(int(input())):
    n = int(input())

    print(dp[n])
