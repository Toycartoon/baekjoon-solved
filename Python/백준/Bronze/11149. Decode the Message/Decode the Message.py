for t in range(int(input())):
    ans = ""
    s = input().split()

    for x in s:
        v = 0
        for i in x:
            v += ord(i) - 97

        v %= 27
        if v < 26:
            ans += chr(v+97)
        else:
            ans += " "

    print(ans)
