from math import inf

for t in range(int(input())):
    k = int(input())
    n = set(map(int, input().split()))

    a = int(input())
    ans = 0
    mn = (inf, -1)
    for i in range(a):
        x, y, z = map(int, input().split())

        if x in n:
            if 0 <= y < 6 or (y == 6 and z == 0):
                temp = y * 60 + z
                ans += 1
                if min(mn[0], temp) == temp:
                    mn = (temp, x)

    print(mn[1], ans)
