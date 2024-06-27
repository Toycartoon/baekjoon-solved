import sys

n = int(input())
ans = 0
for i in range(n):
    c, k = map(int, input().split())
    ans += c * k * pow(2, k-1, 10 ** 9 + 7)

print(ans % (10 ** 9 + 7))
