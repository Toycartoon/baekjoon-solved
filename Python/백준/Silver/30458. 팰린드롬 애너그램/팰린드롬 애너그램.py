n = int(input())
w = {}
s = input()

for i in range(n):
    if n % 2 == 1 and i == n // 2:
        continue

    if s[i] not in w:
        w[s[i]] = 1
    else:
        w[s[i]] += 1

f = True
for i in w.values():
    if i % 2 == 1:
        f = False
        break

if f:
    print("Yes")
else:
    print("No")
