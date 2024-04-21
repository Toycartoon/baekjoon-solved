# ohwphil 그는 신이야!

import sys

input = sys.stdin.readline

n = int(input())
s = input().split()

dp = [[True] * n for _ in range(n)]
for str_len in range(2, len(s) + 1):
    for start in range(len(s)-str_len+1):
        end = start + str_len - 1
        dp[start][end] = (s[start] == s[end]) and dp[start+1][end-1]


for m in range(int(input())):
    s, e = map(int, input().split())
    print(int(dp[s-1][e-1]))
