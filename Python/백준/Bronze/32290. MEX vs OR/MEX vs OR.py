l, r, x = map(int, input().split())

a = set()
for i in range(l, r+1):
    a.add(i | x)


ans = 0
while True:
    if ans not in a:
        print(ans)
        break
    ans += 1
