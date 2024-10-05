n, k = map(int, input().split())

m = [1]
if k == 1:
    print(1)
else:
    for i in range(2, n + 1):
        if n % i == 0:
            m.append(i)

    try:
        print(m[k - 1])
    except IndexError:
        print(0)