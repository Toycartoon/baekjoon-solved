s = input()
pg, ph = 0, 0

for i in s:
    if i in "SAD":
        pg += 1
    if i in "HAPY":
        ph += 1


if pg == ph == 0:
    print("50.00")
else:
    print("{:.02f}".format((ph / (pg + ph)) * 100 + 10 ** -10))
