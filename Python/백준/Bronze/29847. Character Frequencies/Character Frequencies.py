n = int(input())
s = {}
for _ in range(n):
    f = input()
    for i in f:
        if i == " ":
            continue
        try:
            s[i] += 1
        except KeyError:
            s[i] = 1

for i in s.keys():
    print(i, s[i])
