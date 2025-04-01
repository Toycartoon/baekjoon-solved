w = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1}
while True:
    s = input()

    if s == "#":
        break

    ans = 0
    for i in range(len(s)):
        ans += w[s[i]] * (8 ** (len(s)-i-1))

    print(ans)
