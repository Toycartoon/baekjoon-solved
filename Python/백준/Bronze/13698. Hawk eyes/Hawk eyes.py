c = ["b", ".", ".", "B"]
s = input()

for i in s:
    match i:
        case "A":
            c[0], c[1] = c[1], c[0]
        case "B":
            c[0], c[2] = c[2], c[0]
        case "C":
            c[0], c[3] = c[3], c[0]
        case "D":
            c[1], c[2] = c[2], c[1]
        case "E":
            c[1], c[3] = c[3], c[1]
        case "F":
            c[2], c[3] = c[3], c[2]


print(c.index("b")+1)
print(c.index("B")+1)
