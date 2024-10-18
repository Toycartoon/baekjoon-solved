while True:
    try:
        s = input()
        print(s.replace("iiing", "th"))
    except EOFError:
        break