for t in range(int(input())):
    r, c = map(int, input().split())

    if r == c:
        print("dohoon")
    else:
        print("jinseo")
        print(f"{min(r, c)} " * 2)
