for t in range(int(input())):
    w = {"E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "N": 0, "O": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0,
         "X": 0, "Z": 0}

    s = input()
    for i in s:
        w[i] += 1

    r = [0 for _ in range(10)]

    if w["Z"] > 0:
        r[0] += w["Z"]
        w["Z"] = 0
        w["E"] -= r[0]
        w["R"] -= r[0]
        w["O"] -= r[0]
    if w["W"] > 0:
        r[2] += w["W"]
        w["T"] -= r[2]
        w["W"] = 0
        w["O"] -= r[2]
    if w["U"] > 0:
        r[4] += w["U"]
        w["F"] -= r[4]
        w["O"] -= r[4]
        w["U"] = 0
        w["R"] -= r[4]
    if w["X"] > 0:
        r[6] += w["X"]
        w["S"] -= r[6]
        w["I"] -= r[6]
        w["X"] = 0
    if w["G"] > 0:
        r[8] += w["G"]
        w["E"] -= r[8]
        w["I"] -= r[8]
        w["G"] = 0
        w["H"] -= r[8]
        w["T"] -= r[8]

    if w["H"] > 0:
        r[3] += w["H"]
        w["T"] -= r[3]
        w["H"] = 0
        w["R"] -= r[3]
        w["E"] -= r[3] * 2
    if w["F"] > 0:
        r[5] += w["F"]
        w["F"] = 0
        w["I"] -= r[5]
        w["V"] -= r[5]
        w["E"] -= r[5]
    if w["S"] > 0:
        r[7] += w["S"]
        w["S"] = 0
        w["E"] -= r[7] * 2
        w["V"] -= r[7]
        w["N"] -= r[7]

    if w["O"] > 0:
        r[1] += w["O"]
        w["O"] = 0
        w["N"] -= r[1]
        w["E"] -= r[1]
    if w["I"] > 0:
        r[9] += w["N"] // 2
        w["N"] = 0
        w["I"] -= r[9]
        w["E"] -= r[9]

    print(f"Case #{t+1}:", end=" ")
    for i in range(10):
        print(str(i) * r[i], end="")
    print()
