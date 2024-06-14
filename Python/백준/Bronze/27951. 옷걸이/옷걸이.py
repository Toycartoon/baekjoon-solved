n = int(input())
a = list(map(int, input().split()))
u, d = map(int, input().split())

t, p, x = a.count(1), a.count(2), a.count(3)
uneed, dneed = 0, 0
if u - t != 0:
    uneed = u - t
    if uneed > x:
        print('NO')
        exit()

if d - p != 0:
    dneed = d - p
    if dneed > x:
        print('NO')
        exit()

print('YES')
for i in a:
    if i == 1:
        print("U", end="")
    elif i == 2:
        print("D", end="")
    else:
        if uneed > 0:
            print("U", end="")
            uneed -= 1
        elif dneed > 0:
            print("D", end="")
            dneed -= 1
