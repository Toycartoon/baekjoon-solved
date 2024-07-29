for t in range(int(input())):
    n = input()

    ans = 0
    while int(n) != 6174:
        n = int("".join(sorted([*str(n)], reverse=True))) - int("".join(sorted([*str(n)])))
        ans += 1

        if n < 1000:
            n = str(n).zfill(4)

    print(ans)
