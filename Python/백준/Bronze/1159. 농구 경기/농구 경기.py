w = [0 for _ in range(26)]

for n in range(int(input())):
    s = input()
    w[ord(s[0])-97] += 1

f = True
for i in range(26):
    if w[i] >= 5:
        print(chr(i+97), end="")
        f = False

if f:
    print("PREDAJA")
