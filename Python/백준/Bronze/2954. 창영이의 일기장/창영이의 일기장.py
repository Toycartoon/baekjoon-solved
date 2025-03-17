s = input()
i = 0
while i < len(s):
    print(s[i], end="")

    if s[i] in "aeiou":
        i += 2
    i += 1
