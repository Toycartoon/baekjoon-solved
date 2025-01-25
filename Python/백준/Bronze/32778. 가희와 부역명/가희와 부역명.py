s = input()
s = s.split("(")

if len(s) == 1:
    print(s[0])
    print("-")
else:
    print(s[0])
    print(s[1][:-1])