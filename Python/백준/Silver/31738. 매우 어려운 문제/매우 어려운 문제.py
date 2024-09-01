n, m = map(int, input().split())

if n >= m:
    print(0)
else:
    ans = 1
    for i in range(n, 0, -1):
        ans *= i
        ans %= m
        
        if ans == 0:
            break
    
    print(ans)
