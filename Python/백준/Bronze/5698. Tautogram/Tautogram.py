while True:
    s = input().split()

    if s == ['*']:
        break

    f = True
    for i in range(1, len(s)):
        if s[i-1][0].lower() != s[i][0].lower():
            f = False
            break

    if f:
        print("Y")
    else:
        print("N")
