from decimal import Decimal

c = 299792458
a, b = map(Decimal, input().split())
print(round((a + b) / (1 + (a * b / c ** 2)), 10))