g = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0}
t = 0
v = 0

i = 0
s = input()
while i < len(s):
    if s[i] != "F":
        try:
            if s[i + 1] == "+":
                v += g[s[i] + "+"]
                i += 1
            else:
                v += g[s[i]]
        except IndexError:
            v += g[s[i]]

    t += 1
    i += 1

print(v / t)