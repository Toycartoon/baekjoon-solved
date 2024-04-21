from decimal import Decimal, getcontext

getcontext().prec = 100000

a, b = input().split()

print(format(Decimal(a) ** Decimal(b), "f"))