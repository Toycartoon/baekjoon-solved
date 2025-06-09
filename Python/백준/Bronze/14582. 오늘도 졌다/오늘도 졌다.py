u = list(map(int, input().split()))
s = list(map(int, input().split()))

f = False
us = 0
ss = 0
for i in range(9):
    us += u[i]

    if us > ss:
        f = True
        break
    ss += s[i]

print("Yes" if f else "No")
