from collections import deque

n = int(input())
s = input()

ans = []
p = deque()
c = deque()
for i in range(n):
    if s[i] == "P":
        if c:
            ans[c.popleft()] = "P"
            ans.append("C")
        else:
            p.append(i)
            ans.append("P")
    elif s[i] == "C":
        if p:
            ans[p.popleft()] = "C"
            ans.append("P")
        else:
            c.append(i)
            ans.append("C")
    else:
        ans.append(s[i])


print("".join(ans))
