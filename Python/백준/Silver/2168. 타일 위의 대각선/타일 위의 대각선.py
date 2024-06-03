from math import gcd

x, y = map(int, input().split())
print(x + y - gcd(x, y))
