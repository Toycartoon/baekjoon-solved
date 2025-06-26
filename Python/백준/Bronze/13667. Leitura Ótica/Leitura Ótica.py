while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        a = list(map(int, input().split()))
        ans = []

        for v in a:
            if v <= 127:
                ans.append("B")
            else:
                ans.append("W")

        if ans.count("B") != 1:
            print("*")
        else:
            print(chr(ans.index("B")+65))
