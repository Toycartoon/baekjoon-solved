n = int(input())

m = 1
while True:
    c = m + sum(list(map(int, list(str(m)))))
    if c == n:
        print(m)
        break
    elif len(str(c)) > len(str(n)):
        print(0)
        break
    m += 1