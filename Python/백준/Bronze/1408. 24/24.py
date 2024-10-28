now = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))

h = start[0] - now[0]
m = start[1] - now[1]
s = start[2] - now[2]

if s < 0:
    s += 60
    m -= 1
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24

print(f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}")
