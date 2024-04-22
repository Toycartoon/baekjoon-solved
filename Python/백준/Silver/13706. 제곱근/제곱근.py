from decimal import *

getcontext().prec = 800
print(int(Decimal(int(input())) ** Decimal("0.5")))