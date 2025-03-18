ans = 0
for c in range(int(input())):
    s = input()
    ans = max(ans, s.count("for") + s.count("while"))

print(ans)
