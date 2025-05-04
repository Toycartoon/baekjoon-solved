n = int(input())
s = input()

lw = False
up = False
sp = False
nm = False

for i in s:
    if i.islower():
        lw = True
    if i.isupper():
        up = True
    if i.isnumeric():
        nm = True
    if i in "!@#$%^&*()-+":
        sp = True

ans = 0
ans += [lw, up, sp, nm].count(False)

if n + ans < 6:
    ans += 6 - (n + ans)

print(ans)
