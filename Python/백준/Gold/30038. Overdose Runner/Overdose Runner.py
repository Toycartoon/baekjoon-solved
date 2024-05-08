n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]
k = int(input())
mh = list(map(int, input().split()))
md = list(map(int, input().split()))
mexp = list(map(int, input().split()))
s = int(input())
action = input().split()

mon = {}
p = {"x": -1, "y": -1, "atk": 5, "atk_dist": 1, "p": 1, "need_exp": 10, "exp": 0, "lv": 1}
mi = 0
for y in range(n):
    for x in range(m):
        if g[y][x] == "p":
            p["x"] = x
            p["y"] = y
            g[y][x] = "."
        if g[y][x] == "m":
            mon[(x, y)] = [mh[mi], md[mi], mexp[mi]]
            mi += 1


def lv_up():
    if p["exp"] >= p["need_exp"]:
        p["exp"] -= p["need_exp"]
        p["need_exp"] += 10
        p["atk"] += p["lv"]
        p["lv"] += 1
        p["atk_dist"] += 1
        lv_up()


overdose = False
stamina = 0
used_stamina = 0
dose = 0
for c in action:
    if c == "u":
        if 0 <= p["y"] - p["p"]:
            if g[p["y"] - p["p"]][p["x"]] not in "*m":
                p["y"] -= p["p"]

                if overdose:
                    stamina += 1
                used_stamina += 1
    elif c == "d":
        if p["y"] + p["p"] < n:
            if g[p["y"] + p["p"]][p["x"]] not in "*m":
                p["y"] += p["p"]

                if overdose:
                    stamina += 1
                used_stamina += 1
    elif c == "l":
        if 0 <= p["x"] - p["p"]:
            if g[p["y"]][p["x"] - p["p"]] not in "*m":
                p["x"] -= p["p"]

                if overdose:
                    stamina += 1
                used_stamina += 1
    elif c == "r":
        if p["x"] + p["p"] < m:
            if g[p["y"]][p["x"] + p["p"]] not in "*m":
                p["x"] += p["p"]

                if overdose:
                    stamina += 1
                used_stamina += 1
    elif c == "w":
        if overdose:
            stamina += 1
        used_stamina += 1
    elif c == "au":
        if overdose:
            continue
        for y in range(p["y"], max(-1, p["y"] - p["atk_dist"]-1), -1):
            if g[y][p["x"]] == "*":
                break
            if g[y][p["x"]] == "m":
                mon[(p["x"], y)][0] += min(0, mon[(p["x"], y)][1] - p["atk"])

                if mon[(p["x"], y)][0] <= 0:
                    g[y][p["x"]] = "."
                    p["exp"] += mon[(p["x"], y)][2]
        used_stamina += 3
    elif c == "ad":
        if overdose:
            continue
        for y in range(p["y"], min(n, p["y"] + p["atk_dist"]+1)):
            if g[y][p["x"]] == "*":
                break
            if g[y][p["x"]] == "m":
                mon[(p["x"], y)][0] += min(0, mon[(p["x"], y)][1] - p["atk"])

                if mon[(p["x"], y)][0] <= 0:
                    g[y][p["x"]] = "."
                    p["exp"] += mon[(p["x"], y)][2]
        used_stamina += 3
    elif c == "al":
        if overdose:
            continue
        for x in range(p["x"], max(-1, p["x"] - p["atk_dist"]-1), -1):
            if g[p["y"]][x] == "*":
                break
            if g[p["y"]][x] == "m":
                mon[(x, p["y"])][0] += min(0, mon[(x, p["y"])][1] - p["atk"])

                if mon[(x, p["y"])][0] <= 0:
                    g[p["y"]][x] = "."
                    p["exp"] += mon[(x, p["y"])][2]
        used_stamina += 3
    elif c == "ar":
        if overdose:
            continue
        for x in range(p["x"], min(m, p["x"] + p["atk_dist"]+1)):
            if g[p["y"]][x] == "*":
                break
            if g[p["y"]][x] == "m":
                mon[(x, p["y"])][0] += min(0, mon[(x, p["y"])][1] - p["atk"])

                if mon[(x, p["y"])][0] <= 0:
                    g[p["y"]][x] = "."
                    p["exp"] += mon[(x, p["y"])][2]
        used_stamina += 3
    elif c == "du":
        if overdose:
            continue
        
        p["p"] += 1
        dose += 1
        if dose >= 5:
            overdose = True
            dose = 0

        used_stamina += 2
    elif c == "dd":
        if overdose:
            continue

        p["p"] -= 1
        dose += 1
        if p["p"] < 0:
            p["p"] = 0
            
        if dose >= 5:
            overdose = True
            dose = 0

        used_stamina += 2
    elif c == "c":
        if overdose:
            continue
        if g[p["y"]][p["x"]] == "g":
            break

    lv_up()
    if overdose and stamina >= 10:
        overdose = False
        stamina = 0


g[p["y"]][p["x"]] = "p"

print(p["lv"], p["exp"])
print(used_stamina)
for i in g:
    print("".join(i))

final_mh = []
for y in range(n):
    for x in range(m):
        if g[y][x] == "m":
            final_mh.append(str(mon[(x, y)][0]))

print(" ".join(final_mh))
