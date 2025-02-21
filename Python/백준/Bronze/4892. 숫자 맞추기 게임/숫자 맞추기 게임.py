t = 1
while True:
    n = int(input())

    if n == 0:
        break

    n *= 3
    if n % 2 == 0:
        print(f"{t}. even ", end="")
    else:
        print(f"{t}. odd ", end="")

    n = n // 2 if n % 2 == 0 else (n + 1) // 2
    n *= 3

    print(n // 9)
    t += 1
