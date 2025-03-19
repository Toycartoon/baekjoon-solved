s = input()
r = s.index("@")
e = s.index("!")

if r > e:
    r, e = e, r

if s[r:e].count("|") == 0 and s[r:e].count("#") == 1:
    print(e - r - 1)
else:
    print(-1)