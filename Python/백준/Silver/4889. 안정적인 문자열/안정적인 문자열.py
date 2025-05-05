t = 1
while True:
    q = []
    s = input()

    if s.count("-") >= 1:
        break

    for i in s:
        if i == "{":
            q.append("{")
        elif i == "}":
            if len(q) == 0 or q[-1] == "}":
                q.append("}")
            else:
                q.pop()

    ans = 0
    for i in range(0, len(q)-1, 2):
        if q[i] == q[i+1]:
            ans += 1
        else:
            ans += 2

    print(f"{t}. {ans}")
    t += 1
