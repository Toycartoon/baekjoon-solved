from math import comb

n, r = map(int, input().split())
print(comb(n, r) % 1000000007)
