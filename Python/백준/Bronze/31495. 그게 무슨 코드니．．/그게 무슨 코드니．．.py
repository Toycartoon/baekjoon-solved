s = input()

if s[0] == s[-1] == '"':
    if len(s) <= 2:
        print("CE")
    else:
        print(s[1:-1])
else:
    print("CE")
