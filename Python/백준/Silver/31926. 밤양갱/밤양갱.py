n = int(input())

i = 1
while True:
    if 2 ** (i-1) <= n < 2 ** i:
        print(9 + i)
        break
    i += 1
