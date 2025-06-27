s = set()
ans = set()
while True:
    x = input()

    if x == "000-00-0000":
        break

    if x in s:
        ans.add(x)
    else:
        s.add(x)

ans = list(ans)
ans.sort()
for i in ans:
    print(i)
