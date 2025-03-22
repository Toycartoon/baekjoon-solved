import re

n = int(input())
s = input()

p = "s[k_][e_][e_][p_]"

q = []
ans = 0
for i in range(n):
    q.append(s[i])
    while len(q) >= 5 and re.match(p, "".join(q[-5:])):
        for _ in range(5):
            q.pop()
        q.append("_")
        ans += 1

print(ans)
