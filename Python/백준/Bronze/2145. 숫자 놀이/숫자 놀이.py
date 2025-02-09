import sys

input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == 0:
        break
    
    x = list(map(int, [*str(n)]))
    while len(x) > 1:
        a = sum(x)
        x = list(map(int, [*str(a)]))
    
    print(x[0])
