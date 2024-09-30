for _ in range(int(input())):
    s = input()
    A, a = 0, 0
    is_not_num = False

    if len(s) > 10:
        continue

    for i in s:
        if not i.isnumeric():
            is_not_num = True
        if i.isupper():
            A += 1
        if i.islower():
            a += 1

    if A <= a and is_not_num:
        print(s)
        break
