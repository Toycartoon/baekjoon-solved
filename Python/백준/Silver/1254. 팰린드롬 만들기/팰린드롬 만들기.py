s = input()

x = s[::-1]
if s == x:
    print(len(s))
    exit()

for i in range(len(s)):
    if s[i:] == x[:-i]:
        print(len(s + x[-i:]))
        break