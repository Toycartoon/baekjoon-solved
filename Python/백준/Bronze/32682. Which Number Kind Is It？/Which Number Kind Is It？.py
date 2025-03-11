import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    
    o = bool(n % 2 == 1)
    s = bool(int(n ** 0.5) ** 2 == n)
    
    if o and s:
        print("OS")
    elif o:
        print("O")
    elif s:
        print("S")
    else:
        print("EMPTY")