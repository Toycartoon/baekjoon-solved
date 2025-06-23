for t in range(int(input())):
    s = input()

    print(s)
    for i in range(1, len(s)-1):
        print(s[i] + " " * (len(s)-2) + s[-i-1])
    print(s[::-1]) if len(s) > 1 else 0
