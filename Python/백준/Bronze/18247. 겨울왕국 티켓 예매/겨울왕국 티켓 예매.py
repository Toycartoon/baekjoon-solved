for t in range(int(input())):
    n, m = map(int, input().split())
    
    if n < 12 or m < 4:
        print(-1)
    else:
        print(m * 11 + 4)