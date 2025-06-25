import sys

print = sys.stdout.write

a = input()
b = input()

g = [0 for _ in range(26)]
for i in {*a}:
    g[ord(i)-97] = max(g[ord(i)-97], a.count(i))

for i in {*b}:
    g[ord(i)-97] = max(g[ord(i)-97], b.count(i))

for i in range(26):
    print(chr(i+97) * g[i])
