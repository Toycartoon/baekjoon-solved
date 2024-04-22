while True:
    a = input()
    s = []

    if a == ".":
        break

    f = True
    for i in a:
        if i == "(":
            s.append("(")
        elif i == "[":
            s.append("[")
        elif i == ")":
            try:
                if s.pop() != "(":
                    print("no")
                    f = False
                    break
            except IndexError:
                print("no")
                f = False
                break
        elif i == "]":
            try:
                if s.pop() != "[":
                    print("no")
                    f = False
                    break
            except IndexError:
                print("no")
                f = False
                break

    if f:
        if len(s) == 0:
            print("yes")
        else:
            print("no")
