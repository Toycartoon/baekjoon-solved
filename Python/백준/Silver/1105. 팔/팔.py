l, r = map(int, input().split())

a = 0
if len(str(l)) == len(str(r)):
    for i in range(len(str(l))):
        if str(l)[i] == str(r)[i]:
            if str(l)[i] == "8":
                a += 1
        else:
            break

print(a)