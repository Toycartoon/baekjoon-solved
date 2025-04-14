s = input()
x = set()

ans = [13, 13, 13, 13]
for i in range(2, len(s), 3):
    if s[i-2:i+1] in x:
        print("GRESKA")
        exit()

    x.add(s[i-2:i+1])
    match s[i-2]:
        case "P":
            ans[0] -= 1
        case "K":
            ans[1] -= 1
        case "H":
            ans[2] -= 1
        case "T":
            ans[3] -= 1

print(*ans)
