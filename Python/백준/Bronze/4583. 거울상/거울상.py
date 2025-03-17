while True:
    s = input()

    if s == "#":
        break

    a = {"b": "d", "d": "b", "i": "i", "o": "o", "p": "q", "q": "p", "v": "v", "w": "w", "x": "x"}

    ans = ""
    f = True
    for i in range(len(s)-1, -1, -1):
        if s[i] not in a:
            f = False
        else:
            ans += a[s[i]]

    if f:
        print(ans)
    else:
        print("INVALID")
