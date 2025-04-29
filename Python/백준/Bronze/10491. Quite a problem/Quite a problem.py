while True:
    try:
        s = input().lower()
        if "problem" in s:
            print("yes")
        else:
            print("no")
    except EOFError:
        break
