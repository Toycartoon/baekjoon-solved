s = input()
f = "UCPC"
c = 0

for i in range(len(s)):
    if s[i] == f[c]:
        c += 1
        if c == len(f):
            break

if c != len(f):
    print("I hate UCPC")
else:
    print("I love UCPC")