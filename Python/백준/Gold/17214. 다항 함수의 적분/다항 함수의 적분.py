s = input().split("x")

if len(s) == 1:
    if s[0] == "1":
        print("x+W")
    elif s[0] == "-1":
        print("-x+W")
    elif s[0] == "0":
        print("W")
    else:
        print(s[0] + "x+W")
else:
    if s[1] == "":
        if int(s[0]) // 2 == 1:
            print("xx+W")
        elif int(s[0]) // 2 == -1:
            print("-xx+W")
        else:
            print(f"{int(s[0]) // 2}xx+W")
    elif s[1] == "1":
        if int(s[0]) // 2 == 1:
            print("xx+x+W")
        elif int(s[0]) // 2 == -1:
            print("-xx+x+W")
        else:
            print(f"{int(s[0]) // 2}xx+x+W")
    elif s[1] == "-1":
        if int(s[0]) // 2 == 1:
            print("xx-x+W")
        elif int(s[0]) // 2 == -1:
            print("-xx-x+W")
        else:
            print(f"{int(s[0]) // 2}xx-x+W")
    else:
        if int(s[0]) // 2 == 1:
            if s[1] == "+1":
                print("xx+x+W")
            elif s[1] == "-1":
                print("xx-x+W")
            else:
                print(f"xx{s[1]}x+W")
        elif int(s[0]) // 2 == -1:
            if s[1] == "+1":
                print("-xx+x+W")
            elif s[1] == "-1":
                print("-xx-x+W")
            else:
                print(f"-xx{s[1]}x+W")
        else:
            if s[1] == "+1":
                print(f"{int(s[0]) // 2}xx+x+W")
            elif s[1] == "-1":
                print(f"{int(s[0]) // 2}xx-x+W")
            else:
                print(f"{int(s[0]) // 2}xx{s[1]}x+W")