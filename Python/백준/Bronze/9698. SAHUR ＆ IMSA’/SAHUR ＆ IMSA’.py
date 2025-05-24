for t in range(int(input())):
    h, m = map(int, input().split())
    m -= 45
    if m < 0:
        h -= 1
        m += 60

    if h < 0:
        h += 24

    print(f"Case #{t+1}: {h} {m}")
