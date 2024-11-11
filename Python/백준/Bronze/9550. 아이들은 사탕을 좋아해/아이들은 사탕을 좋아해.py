for t in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    
    for i in l:
        ans += i // k
    
    print(ans)