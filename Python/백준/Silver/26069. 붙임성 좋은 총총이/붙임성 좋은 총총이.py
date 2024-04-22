d = ["ChongChong"]
for _ in range(int(input())):
    a, b = input().split()
    if a in d:
        if not b in d:
            d.append(b)
    elif b in d:
        if not a in d:
            d.append(a)

print(len(d))