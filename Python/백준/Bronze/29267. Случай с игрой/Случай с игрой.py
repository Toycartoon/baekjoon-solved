n, k = map(int, input().split())
ammo = 0
save = 0
for i in range(n):
    s = input()

    if s == "ammo":
        ammo += k
    elif s == "save":
        save = ammo
    elif s == "load":
        ammo = save
    elif s == "shoot" and ammo > 0:
        ammo -= 1

    print(ammo)
