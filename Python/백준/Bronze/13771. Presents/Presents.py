ans = []
for n in range(int(input())):
    ans.append(float(input()))

ans.sort()
print(f"{ans[1]:.02f}")
