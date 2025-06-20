pi = 3.14159

ans = 0
for t in range(int(input())):
    s = input().split()

    match s[0]:
        case "S":
            ans = max(ans, (4 / 3) * pi * float(s[1]) ** 3)
        case "C":
            ans = max(ans, (1 / 3) * pi * float(s[1]) ** 2 * float(s[2]))
        case "L":
            ans = max(ans, pi * float(s[1]) ** 2 * float(s[2]))

print(f"{ans:.3f}")
