n = input()
s = ""
i = 1
a = 0
while True:
    s += str(i)
    a += len(str(i))
    if s != n[:a]:
        print(-1)
        break
    elif s == n:
        print(i)
        break
    else:
        i += 1
