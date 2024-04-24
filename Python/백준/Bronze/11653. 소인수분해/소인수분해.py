n = int(input())
num = []
d_n = 2

if n == 1:
    print()
else:
    while n != 1:
        if n % d_n == 0:
            num.append(d_n)
            n = n / d_n
            continue
        else:
            d_n += 1

    for i in num:
        print(i)
