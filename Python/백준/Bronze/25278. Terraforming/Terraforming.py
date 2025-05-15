n = int(input())
ocean = 0
oxygen = 0
temperature = -30

for i in range(n):
    s = input().split()

    match s[0]:
        case "ocean":
            ocean = eval("".join(s))
        case "oxygen":
            oxygen = eval("".join(s))
        case "temperature":
            temperature = eval("".join(s))

if ocean >= 9 and oxygen >= 14 and temperature >= 8:
    print("liveable")
else:
    print("not liveable")
