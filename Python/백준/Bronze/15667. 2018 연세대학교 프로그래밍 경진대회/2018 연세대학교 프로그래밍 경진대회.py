n = int(input())

k = 1
while True:
    if k + k ** 2 == n - 1:
        print(k)
        break
    k += 1
