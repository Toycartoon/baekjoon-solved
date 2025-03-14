n = int(input())
s = input()

g = ["ABC", "BABC", "CCAABB"]

a = 0
b = 0
c = 0
for i in range(n):
    if g[0][i % 3] == s[i]:
        a += 1
    if g[1][i % 4] == s[i]:
        b += 1
    if g[2][i % 6] == s[i]:
        c += 1

m = max(a, b, c)
print(m)
if m == a:
    print("Adrian")
if m == b:
    print("Bruno")
if m == c:
    print("Goran")
