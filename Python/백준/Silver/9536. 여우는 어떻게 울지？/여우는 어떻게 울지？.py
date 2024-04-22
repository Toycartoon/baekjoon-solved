for _ in range(int(input())):
    s = input().split()
    while True:
        a = input()
        if a == "what does the fox say?":
            break
        for i in range(len(s)):
            if a.split()[2] == s[i]:
                s[i] = ""

    for i in s:
        if i != "":
            print(i, end=" ")
    print()