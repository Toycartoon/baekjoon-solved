from collections import deque

ans = []
for n in range(int(input())):
    s = deque([*input()])

    f = False
    for i in range(len(s)):
        if s in ans:
            f = True
            break

        s.rotate(-1)

    if not f:
        ans.append(s)

print(len(ans))
