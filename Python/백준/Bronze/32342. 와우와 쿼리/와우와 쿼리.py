for q in range(int(input())):
    s = input()

    ans = 0
    for i in range(len(s)-2):
        if s[i:i+3] == "WOW":
            ans += 1

    print(ans)
