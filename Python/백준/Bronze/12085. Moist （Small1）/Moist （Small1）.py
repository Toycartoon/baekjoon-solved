for t in range(int(input())):
    ans = 0
    l = []
    for n in range(int(input())):
        l.append(input())

    x = 0
    for i in range(1, len(l)):
        if l[i] < l[x]:
            ans += 1
        else:
            x = i


    print(f"Case #{t+1}: {ans}")
