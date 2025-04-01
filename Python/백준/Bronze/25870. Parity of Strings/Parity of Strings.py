w = [0 for _ in range(26)]
s = input()

for i in s:
    w[ord(i)-97] += 1

f = w[ord(s[0])-97] % 2
for i in w:
    if i == 0:
        continue

    if i % 2 != f:
        f = 2
        break

print(f)
