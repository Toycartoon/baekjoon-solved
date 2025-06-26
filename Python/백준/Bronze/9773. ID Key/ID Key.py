for t in range(int(input())):
    s = input()

    a = sum(list(map(int, [*s])))
    b = int(s[-3:]) * 10

    ans = str(a + b)[-4:]
    if len(ans) < 4:
        ans = str(1000 + int(ans))

    print(ans)
