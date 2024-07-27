for t in range(int(input())):
    n, a, d = map(int, input().split())
    
    ans = 0
    x = a
    for i in range(n):
        ans += x
        x += d
    
    print(ans)