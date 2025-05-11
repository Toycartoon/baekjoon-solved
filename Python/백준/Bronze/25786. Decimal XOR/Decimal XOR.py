a = input()
b = input()

a = a.zfill(max(len(a), len(b)))
b = b.zfill(max(len(a), len(b)))

for i in range(len(a)):
    if (int(a[i]) <= 2 and int(b[i]) <= 2) or (int(a[i]) >= 7 and int(b[i]) >= 7):
        print(0, end="")
    else:
        print(9, end="")
