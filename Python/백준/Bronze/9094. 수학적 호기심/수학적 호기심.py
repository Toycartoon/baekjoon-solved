import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    
    ans = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if ((a ** 2 + b ** 2 + m) / (a * b)).is_integer():
                ans += 1
    
    print(ans)