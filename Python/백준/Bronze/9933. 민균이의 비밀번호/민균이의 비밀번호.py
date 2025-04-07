p = []
for n in range(int(input())):
    p.append(input())

ans = []
for i in p:
    if len(i) % 2 == 1 and i[::-1] in p:
        ans.append(i)


print(len(ans[0]), ans[0][len(ans[0])//2])
