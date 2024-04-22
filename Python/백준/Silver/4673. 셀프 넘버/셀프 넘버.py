def d(n):
    if n < 10:
        return n + n
    else:
        return n + sum(int(i) for i in str(n))

l = [i for i in range(1, 10001)]

for i in range(1, 10001):
    to_blank = d(i)
    if to_blank - 1 >= 10000:
        pass
    else:
        l[to_blank - 1] = 0

for i in l:
    if i == 0:
        pass
    else:
        print(i)