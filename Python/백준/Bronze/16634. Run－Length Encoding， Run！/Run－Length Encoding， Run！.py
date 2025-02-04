c, s = input().split()

if c == "D":
    for i in range(len(s)):
        if s[i].isnumeric():
            print(s[i-1] * int(s[i]), end="")
elif c == "E":
    x = 1

    print(s[0], end="")
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            print(x, end=s[i])
            x = 0
        x += 1

    print(x)
