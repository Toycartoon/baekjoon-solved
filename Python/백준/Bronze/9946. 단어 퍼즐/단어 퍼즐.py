i = 1
while True:
    s = input()
    t = input()

    if s == t == "END":
        break

    s = sorted([*s])
    t = sorted([*t])

    if s == t:
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")

    i += 1
