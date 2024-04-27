n = []
for _ in range(int(input())):
    s = input()
    if len(s) == 3:
        n.append(s)

print(sorted(n)[0])