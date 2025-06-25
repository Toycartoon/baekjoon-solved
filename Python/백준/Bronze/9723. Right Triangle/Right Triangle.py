for t in range(int(input())):
    x = list(map(int, input().split()))

    x.sort()
    print(f"Case #{t+1}: ", end="")
    if x[0] ** 2 + x[1] ** 2 == x[-1] ** 2:
        print("YES")
    else:
        print("NO")
