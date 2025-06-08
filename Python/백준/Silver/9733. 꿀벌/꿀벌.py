w = {"Re": 0, "Pt": 0, "Cc": 0, "Ea": 0, "Tb": 0, "Cm": 0, "Ex": 0}

tot = 0
while True:
    try:
        a = input().split()
        for i in a:
            if i in w:
                w[i] += 1
            tot += 1
    except EOFError:
        break

for i in w:
    print(i, w[i], f"{w[i] / tot:.02f}")

print(f"Total {tot} 1.00")
