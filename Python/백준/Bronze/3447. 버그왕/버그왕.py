while True:
    try:
        s = input()
        while True:
            t = s.replace("BUG", "")
            if t == s:
                print(t)
                break
            s = t
    except EOFError:
        break
