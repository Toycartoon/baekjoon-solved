bh, bm, bs = map(int, input().split(":"))
h, m, s = map(int, input().split(":"))

if bh == h and bm == m and bs == s:
    print("24:00:00")
    exit()

s -= bs
if s < 0:
    s += 60
    m -= 1

m -= bm
if m < 0:
    m += 60
    h -= 1

h -= bh
if h < 0:
    h += 24

print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")
