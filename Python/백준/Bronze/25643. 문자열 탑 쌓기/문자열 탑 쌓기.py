n, m = map(int, input().split())
b = input()

ans = True
for i in range(n-1):
    s = input()

    f = True
    for x in range(m):
        if b[m-x-1:] == s[:x+1]:
            f = False
            break

    for x in range(m-2, -1, -1):
        if b[:x+1] == s[m-x-1:]:
            f = False
            break

    if f:
        ans = False
        break
    b = s


print(int(ans))
