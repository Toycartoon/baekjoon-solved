from decimal import *

getcontext().prec = 1000

for _ in range(int(input())):
    n = Decimal(input())
    ans = Decimal(n ** (Decimal("1") / Decimal("3")))
    ans = str(round(ans, 500))
    print(ans[:len(ans)-490])
