for t in range(int(input())):
    s = input()

    x = s[::-1]
    if s == x:
        print(s)
        continue

    for i in range(len(s)):
        if s[i:] == x[:-i]:
            print(s + x[-i:])
            break
