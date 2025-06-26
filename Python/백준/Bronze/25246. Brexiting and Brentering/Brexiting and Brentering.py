s = input()

for i in range(len(s)):
    if s[::-1][i] in "aeiou":
        s = ("yrtn" + s[::-1][i:])[::-1]
        break

print(s)
