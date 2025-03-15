import sys
from decimal import Decimal as d

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    x = (d("3.0") + (d("5.0") ** d("0.5"))) ** d(n)
    print(f"Case #{t+1}: {str(x).split(".")[0][-3:].zfill(3)}")
