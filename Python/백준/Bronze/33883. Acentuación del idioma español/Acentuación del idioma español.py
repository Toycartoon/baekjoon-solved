s = input()

s = s[::-1]
if s[0] in "aeiouns":
    f = True
    for i in range(len(s)):
        if s[i] in "aeiou":
            if f:
                f = False
            else:
                print(len(s)-i)
                exit()
else:
    for i in range(len(s)):
        if s[i] in "aeiou":
            print(len(s)-i)
            exit()

print(-1)
