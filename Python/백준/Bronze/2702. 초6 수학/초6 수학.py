from math import *

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b), gcd(a, b))