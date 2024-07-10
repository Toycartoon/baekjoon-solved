i = 1
while True:
    l, p, v = map(int, input().split())

    if l == p == v == 0:
        break

    print(f"Case {i}: {(v // p) * l + min(l, v % p)}")
    i += 1
