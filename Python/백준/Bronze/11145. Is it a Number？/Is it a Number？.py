for t in range(int(input())):
    try:
        s = input().strip()

        if len(s) == 0 or not s[0].isdigit():
            raise ValueError

        s = int(s)

        if s < 0:
            print("invalid input")
        else:
            print(s)
    except ValueError:
        print("invalid input")
