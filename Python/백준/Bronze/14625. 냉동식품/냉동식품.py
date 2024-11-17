sh, sm = map(int, input().split())
eh, em = map(int, input().split())
n = input()

h, m = sh, sm
ans = int(n in str(h).zfill(2) + str(m).zfill(2))
while (h, m) != (eh, em):
    m += 1

    if m >= 60:
        h += 1
        m = 0

    if n in str(h).zfill(2) + str(m).zfill(2):
        ans += 1


print(ans)