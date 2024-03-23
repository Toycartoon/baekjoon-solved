n = int(input())

a = 0
i = a
while True:
    if n - ((6 * i) + 1) <= 0:
        print(a + 1)
        break
    a += 1
    i += a