from collections import deque

n, s, w, g = map(int, input().split())
m = ["" for _ in range((4 * n) - 4)]
bought = [False for _ in range((4 * n) - 4)]
m[0] = "S"
bought[0] = True
m[n-1] = "I"
bought[n-1] = True
m[2*n-2] = "O"
bought[2*n-2] = True
m[3*n-3] = "T"
bought[3*n-3] = True

k = deque()
for _ in range(g):
    k.append(tuple(map(int, input().split())))

for i in range(len(m)):
    if m[i] == "":
        l, *c = input().split()
        if not c:
            c = "0"
            bought[i] = True
        m[i] = (l, int(c[0]))

p = 0
isolated = -1
money = s
s_fund = 0
for i in range(int(input())):
    x, y = map(int, input().split())

    if isolated != -1:
        if x != y:
            isolated -= 1
            continue
        else:
            isolated = -1
            continue

    p += x + y
    if p >= 4 * n - 4:
        money += w * (p // (4 * n - 4))
        p %= (4 * n - 4)

    if m[p][0] == "G":
        com = k.popleft()

        if com[0] == 1:
            money += com[1]
        elif com[0] == 2:
            if money < com[1]:
                print("LOSE")
                exit()
            money -= com[1]
        elif com[0] == 3:
            if money < com[1]:
                print("LOSE")
                exit()
            s_fund += com[1]
            money -= com[1]
        elif com[0] == 4:
            p += com[1]
            if p >= 4 * n - 4:
                money += w * (p // (4 * n - 4))
                p %= 4 * n - 4
        k.append(com)

    if m[p][0] == "I":
        isolated = 2
    elif m[p][0] == "O":
        money += s_fund
        s_fund = 0
    elif m[p][0] == "T":
        money += w
        p = 0
    elif m[p][0] == "L":
        if money >= m[p][1] and not bought[p]:
            money -= m[p][1]
            bought[p] = True


f = False
for i in bought:
    if not i:
        f = True

if f:
    print("LOSE")
else:
    print("WIN")
