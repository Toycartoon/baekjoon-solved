for t in range(int(input())):
    n = int(input())

    a = str(n ** 2)
    if int(a[-len(str(n))::]) == n:
        print("YES")
    else:
        print("NO")
