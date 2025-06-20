n = input()
while True:
    if int(n) % sum(map(int, [*n])) == 0:
        print(n)
        break

    n = str(int(n) + 1)
