s = input()

if len(set([*s])) == 1:
    print(-1)
elif s == s[::-1]:
    print(len(s)-1)
else:
    print(len(s))
