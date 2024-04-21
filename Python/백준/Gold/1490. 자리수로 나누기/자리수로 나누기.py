n = input()
i = -1
s = 1
while True:
    if i > int("9" * s):
        s += 1
        i = 0
        continue

    f = True
    a = n + (str(i).zfill(s) if i != -1 else "")
    for j in n:
        if j == "0":
            continue
        if int(a) % int(j) != 0:
            f = False
    if f:
        print(a)
        break
    i += 1