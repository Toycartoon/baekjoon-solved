from math import isqrt
import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    
    if isqrt(n) ** 2 == n and (isqrt(int(str(n)[::-1])) ** 2) == int(str(n)[::-1]):
        print("YES")
    else:
        print("NO")