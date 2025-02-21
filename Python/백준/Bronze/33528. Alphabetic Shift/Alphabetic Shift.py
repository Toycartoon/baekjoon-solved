s = input()

for i in range(26):
    for x in s:
        print(chr(ord(x)-i if ord(x)-i >= 65 else ord(x)-i+26), end="")
    print()
