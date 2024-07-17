for _ in range(int(input())):
    s = input()
    a = [False] * 26

    for i in s:
        if i.isalpha():
            a[ord(i.lower()) - 97] = True

    if a.count(True) == 26:
        print("pangram")
    else:
        print("missing ", end="")
        for i in range(26):
            if not a[i]:
                print(chr(i + 97), end="")
        print()
