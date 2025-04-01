for t in range(int(input())):
    w = {}
    for i in input().split(","):
        s, a = i.split(":")
        w[s] = int(a)

    x = input().split("|")

    ans = []
    for i in x:
        v = 0
        for j in i.split("&"):
            v = max(v, w[j])

        ans.append(v)
    print(min(ans))
