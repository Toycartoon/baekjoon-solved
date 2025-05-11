while True:
    n = input()

    if n == "0":
        break

    s = len(n)
    ans = 0
    while str(int(n) + ans).zfill(s) != str(int(n) + ans).zfill(s)[::-1]:
        ans += 1

    print(ans)
