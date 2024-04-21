cs = []
for _ in range(int(input())):
    c, a, t = input().split()
    cs.append([c, a, int(t)])

for i in range(len(cs) - 1, -1, -1):
    if cs[i][0] == "undo":
        for j in range(i, -1, -1):
            if cs[j][2] >= cs[i][2] - int(cs[i][1]):
                cs[j][0] = "-"

for com in cs:
    if com[0] != "-":
        print(com[1], end="")