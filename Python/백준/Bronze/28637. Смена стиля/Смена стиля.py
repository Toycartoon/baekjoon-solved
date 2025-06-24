for t in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[i].isupper():
            if i != 0:
                print('_', end="")
            print(s[i].lower(), end="")
        else:
            print(s[i], end="")
    print()
