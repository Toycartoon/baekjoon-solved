import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    ans = n
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
            ans = max(ans, n)
    
    print(ans)
