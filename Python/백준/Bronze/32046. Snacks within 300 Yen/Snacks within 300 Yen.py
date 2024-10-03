import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
        
    a = list(map(int, input().split()))
    
    ans = 0
    for i in a:
        if ans + i <= 300:
            ans += i
    
    print(ans)
