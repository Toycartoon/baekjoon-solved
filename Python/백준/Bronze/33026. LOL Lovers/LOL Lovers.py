n = int(input())
s = input()
f = False
for i in range(1, n):
    if s[:i].count("L") != s[i:].count("L") and s[:i].count("O") != s[i:].count("O"):
        f = True
        print(i)
        break

if not f:
    print(-1)
