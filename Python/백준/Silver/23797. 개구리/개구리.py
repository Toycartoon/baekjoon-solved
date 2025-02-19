s = input()

ans = {"K": 0, "P": 0}
for i in s:
    if i == "K":
        if ans["P"] > 0:
            ans["P"] -= 1
            ans["K"] += 1
        else:
            ans["K"] += 1
    elif i == "P":
        if ans["K"] > 0:
            ans["K"] -= 1
            ans["P"] += 1
        else:
            ans["P"] += 1


print(sum(ans.values()))
