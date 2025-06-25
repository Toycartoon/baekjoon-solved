while True:
    try:
        a = list(map(int, input().split()))
        ans = []
        for i in range(len(a)):
            if i == 0:
                ans.append(a[i+1] * a[i])
            elif i == len(a)-1:
                ans.append(a[i] * a[i-1])
            else:
                ans.append(a[i-1] * a[i] * a[i+1])

        print(*ans)
    except EOFError:
        break
