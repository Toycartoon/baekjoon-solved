v = {}
while True:
    s = input()

    if s == "0":
        break

    if s in v:
        v[s] += 1
    else:
        v[s] = 1

for i in v:
    print(f"{i}: {v[i]}")
print(f"Grand Total: {sum(v.values())}")
