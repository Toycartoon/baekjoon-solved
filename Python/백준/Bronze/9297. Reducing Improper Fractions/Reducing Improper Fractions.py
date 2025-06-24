for t in range(int(input())):
    n, d = map(int, input().split())

    if n % d == 0:
        print(f"Case {t+1}: {n // d}")
    elif n // d == 0:
        print(f"Case {t+1}: {n}/{d}")
    else:
        print(f"Case {t+1}: {n // d} {n % d}/{d}")
