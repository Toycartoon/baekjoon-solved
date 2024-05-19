s = input()
t = input()

q = []
for i in s:
    q.append(i)
    if q[len(q)-len(t):] == [*t]:
        for _ in range(len(t)):
            q.pop()

print("".join(q))
