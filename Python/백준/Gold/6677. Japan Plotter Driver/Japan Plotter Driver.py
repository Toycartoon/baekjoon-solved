def checker(x, y, type):
    if g[y][x] == " " or g[y][x] == type:
        return type
    if g[y][x] == "-" and type == "|" or g[y][x] == "|" and type == "-" or g[y][x] == "+" and type in "-|":
        return "+"
    if g[y][x] == "/" and type == "\\" or g[y][x] == "\\" and type == "/" or g[y][x] == "x" and type in "/\\":
        return "x"
    return "*"


while True:
    x, y = map(int, input().split())

    if x == y == 0:
        break

    g = [[" " for i in range(x)] for _ in range(y)]
    while True:
        com, *c = input().split()

        if com == "PRINT":
            break
        elif com == "POINT":
            g[int(c[1])-1][int(c[0])-1] = checker(int(c[0])-1, int(c[1])-1, "o")
        elif com == "TEXT":
            txt = c[2]
            for i in range(len(txt)):
                if int(c[0])+i > x:
                    break
                else:
                    g[int(c[1])-1][int(c[0])-1+i] = checker(int(c[0])-1+i, int(c[1])-1, txt[i])
        elif com == "LINE":
            if c[1] == c[3]:
                if int(c[0]) > int(c[2]):
                    c[0], c[2] = c[2], c[0]

                for i in range(int(c[0])-1, int(c[2])):
                    g[int(c[1])-1][i] = checker(i, int(c[1])-1, "-")
            elif c[0] == c[2]:
                if int(c[1]) > int(c[3]):
                    c[1], c[3] = c[3], c[1]

                for i in range(int(c[1])-1, int(c[3])):
                    g[i][int(c[0])-1] = checker(int(c[0])-1, i, "|")
            else:
                if int(c[0]) > int(c[2]):
                    c[0], c[1], c[2], c[3] = c[2], c[3], c[0], c[1]
                    
                if int(c[1]) < int(c[3]):
                    for i in range(0, int(c[2])-int(c[0])+1):
                        g[int(c[1])-1+i][int(c[0])-1+i] = checker(int(c[0])-1+i, int(c[1])-1+i, "\\")
                else:
                    for i in range(int(c[2])-int(c[0]), -1, -1):
                        g[int(c[1])-1-i][int(c[0])-1+i] = checker(int(c[0])-1+i, int(c[1])-1-i, "/")
        elif com == "CLEAR":
            if int(c[0]) > int(c[2]):
                c[0], c[2] = c[2], c[0]
            if int(c[1]) > int(c[3]):
                c[1], c[3] = c[3], c[1]

            for dy in range(int(c[1])-1, int(c[3])):
                for dx in range(int(c[0])-1, int(c[2])):
                    g[dy][dx] = " "

    print("+" + "-" * x + "+")
    for i in g:
        print("|" + "".join(i) + "|")

    print("+" + "-" * x + "+\n")
