from math import gcd

n = int(input())
a = list(map(int, input().split()))
x = int(input())

ans = []
for i in a:
    if gcd(i, x) == 1:
        ans.append(i)

print(sum(ans) / len(ans))
