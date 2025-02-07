import sys

input = sys.stdin.readline

for t in range(int(input())):
    x, a = map(int, input().split())
    
    x = bin(x)
    if x.count("1") % 2 == a:
        print("Valid")
    else:
        print("Corrupt")