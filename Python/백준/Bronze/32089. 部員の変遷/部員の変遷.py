while True:
    n = int(input())
    if n == 0:
        break
        
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n-2):
        ans = max(ans, sum(a[i:i+3]))

    print(ans)