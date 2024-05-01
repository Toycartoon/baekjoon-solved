e, s, m = map(int, input().split())

de, ds, dm = 0, 0, 0
ans = 0
while True:
    ans += 1
    de += 1
    ds += 1
    dm += 1

    if de > 15:
        de -= 15
    if ds > 28:
        ds -= 28
    if dm > 19:
        dm -= 19

    if (de, ds, dm) == (e, s, m):
        print(ans)
        break
