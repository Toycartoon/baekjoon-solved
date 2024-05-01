priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
q = []

s = input()
for i in s:
    if i.isalpha():
        print(i, end="")
    else:
        if len(q) != 0:
            if i == ")":
                while q:
                    x = q.pop()
                    if x == "(":
                        break
                    print(x, end="")
            elif i == "(" or priority[i] > priority[q[-1]]:
                q.append(i)
            else:
                while q and priority[i] <= priority[q[-1]]:
                    x = q.pop()
                    if x != "(":
                        print(x, end="")
                q.append(i)
        else:
            q.append(i)

while q:
    print(q.pop(), end="")
