import sys
import math

input = sys.stdin.readline


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rex = x
        self.rey = y

        self.max_hp = 20
        self.hp = 20
        self.atk = 2
        self.de = 2

        self.lv = 1
        self.exp = 0
        self.need_exp = 5 * self.lv

        self.weapon = 0
        self.armor = 0
        self.acce = []

    def isdead(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def lvup(self):
        if self.exp >= self.need_exp:
            self.lv += 1

            self.need_exp = 5 * self.lv
            self.exp = 0

            self.max_hp += 5
            self.hp = self.max_hp

            self.atk += 2
            self.de += 2


class Monster:
    def __init__(self, s, w, a, h, e):
        self.name = s
        self.atk = w
        self.de = a
        self.hp = h
        self.max_hp = h
        self.exp = e

    def isdead(self):
        if self.hp <= 0:
            return True
        else:
            return False


def Print_result(killed, turn):
    if killed == "W I N" or killed == "D R A W":
        g[p.y][p.x] = "@"

    for i in g:
        print("".join(i))

    print(f"Passed Turns : {turn}")
    print(f"LV : {p.lv}")
    print(f"HP : {max(0, p.hp)}/{p.max_hp}")
    print(f"ATT : {p.atk}+{p.weapon}")
    print(f"DEF : {p.de}+{p.armor}")
    print(f"EXP : {p.exp}/{p.need_exp}")

    if killed == "W I N":
        print("YOU WIN!")
    elif killed == "D R A W":
        print("Press any key to continue.")
    else:
        print(f"YOU HAVE BEEN KILLED BY {killed}..")


n, m = map(int, input().split())
g = [[*input().strip()] for _ in range(n)]
k = 0
l = 0
for y in range(n):
    for x in range(m):
        if g[y][x] in "&M":
            k += 1
        elif g[y][x] == "@":
            g[y][x] = "."
            p = Player(x, y)
        elif g[y][x] == "B":
            l += 1

s = input().strip()
monster = {}
for i in range(k):
    r, c, name, w, a, h, e = input().split()
    monster[(int(r) - 1, int(c) - 1)] = Monster(name, int(w), int(a), int(h), int(e))

item = {}
for i in range(l):
    r, c, t, val = input().split()
    item[(int(r) - 1, int(c) - 1)] = (t, val)

t = 0
for com in s:
    if com == "L" and p.x > 0:
        if g[p.y][p.x - 1] != "#":
            p.x -= 1
    elif com == "R" and p.x < m - 1:
        if g[p.y][p.x + 1] != "#":
            p.x += 1
    elif com == "U" and p.y > 0:
        if g[p.y - 1][p.x] != "#":
            p.y -= 1
    elif com == "D" and p.y < n - 1:
        if g[p.y + 1][p.x] != "#":
            p.y += 1

    if g[p.y][p.x] == "B":
        if item[(p.y, p.x)][0] == "W":
            p.weapon = int(item[(p.y, p.x)][1])
        elif item[(p.y, p.x)][0] == "A":
            p.armor = int(item[(p.y, p.x)][1])
        elif item[(p.y, p.x)][0] == "O":
            if len(p.acce) < 4 and item[(p.y, p.x)][1] not in p.acce:
                p.acce.append(item[(p.y, p.x)][1])

        g[p.y][p.x] = "."
    elif g[p.y][p.x] == "^":
        if "DX" in p.acce:
            p.hp -= 1
        else:
            p.hp -= 5

        if p.isdead():
            if "RE" not in p.acce:
                Print_result("SPIKE TRAP", t + 1)
                exit()
            else:
                p.acce.remove("RE")
                p.x = p.rex
                p.y = p.rey
                p.hp = p.max_hp
    elif g[p.y][p.x] == "&":
        first_atk = "CO" in p.acce
        while monster[(p.y, p.x)].hp > 0 and p.hp > 0:
            if first_atk:
                first_atk = False
                if "DX" in p.acce:
                    monster[(p.y, p.x)].hp -= max(1, (p.weapon + p.atk) * 3 - monster[(p.y, p.x)].de)
                else:
                    monster[(p.y, p.x)].hp -= max(1, (p.weapon + p.atk) * 2 - monster[(p.y, p.x)].de)
            else:
                monster[(p.y, p.x)].hp -= max(1, (p.weapon + p.atk) - monster[(p.y, p.x)].de)

            if monster[(p.y, p.x)].isdead():
                if "EX" in p.acce:
                    p.exp += math.floor(monster[(p.y, p.x)].exp * 1.2)
                else:
                    p.exp += monster[(p.y, p.x)].exp

                p.lvup()
                g[p.y][p.x] = "."
                if "HR" in p.acce:
                    p.hp = min(p.max_hp, p.hp + 3)
                break

            p.hp -= max(1, monster[(p.y, p.x)].atk - (p.de + p.armor))
            if p.isdead():
                if "RE" not in p.acce:
                    Print_result(monster[(p.y, p.x)].name, t + 1)
                    exit()
                else:
                    p.acce.remove("RE")
                    monster[(p.y, p.x)].hp = monster[(p.y, p.x)].max_hp
                    p.x = p.rex
                    p.y = p.rey
                    p.hp = p.max_hp
                    break
    elif g[p.y][p.x] == "M":
        hu = "HU" in p.acce
        if hu:
            p.hp = p.max_hp
        first_atk = "CO" in p.acce
        while monster[(p.y, p.x)].hp > 0 and p.hp > 0:
            if first_atk:
                first_atk = False
                if "DX" in p.acce:
                    monster[(p.y, p.x)].hp -= max(1, (p.weapon + p.atk) * 3 - monster[(p.y, p.x)].de)
                else:
                    monster[(p.y, p.x)].hp -= max(1, (p.weapon + p.atk) * 2 - monster[(p.y, p.x)].de)
            else:
                monster[(p.y, p.x)].hp -= max(1, (p.weapon + p.atk) - monster[(p.y, p.x)].de)

            if monster[(p.y, p.x)].isdead():
                if "EX" in p.acce:
                    p.exp += math.floor(monster[(p.y, p.x)].exp * 1.2)
                else:
                    p.exp += monster[(p.y, p.x)].exp

                p.lvup()
                g[p.y][p.x] = "."
                if "HR" in p.acce:
                    p.hp = min(p.max_hp, p.hp + 3)
                Print_result("W I N", t + 1)
                exit()

            if hu:
                hu = False
            else:
                p.hp -= max(1, monster[(p.y, p.x)].atk - (p.de + p.armor))
            if p.isdead():
                if "RE" not in p.acce:
                    Print_result(monster[(p.y, p.x)].name, t + 1)
                    exit()
                else:
                    p.acce.remove("RE")
                    monster[(p.y, p.x)].hp = monster[(p.y, p.x)].max_hp
                    p.x = p.rex
                    p.y = p.rey
                    p.hp = p.max_hp
                    break

    t += 1


Print_result("D R A W", t)
