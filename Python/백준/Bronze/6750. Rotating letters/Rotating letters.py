f = True
for i in input():
    if i not in "IOSHXZN":
        f = False
        break
print("YES" if f else "NO")