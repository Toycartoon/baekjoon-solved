for t in range(int(input())):
    s = input()
    a = [0] * 26

    for i in s:
        if i == " ":
            continue
        else:
            a[ord(i)-97] += 1

    if a.count(max(a)) > 1:
        print("?")
    else:
        print(chr(a.index(max(a)) + 97))
