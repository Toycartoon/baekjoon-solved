import sys

input = sys.stdin.readline

q = []
r = 0

c = []
for n in range(int(input())):
    c.append(input().split())

a = 0
while a < len(c):
    com, *x = c[a]

    if com == "PUSH":
        q.append(int(x[0]))
    elif com == "STORE":
        r = q.pop()
    elif com == "LOAD":
        q.append(r)
    elif com == "PLUS":
        i = q.pop()
        j = q.pop()
        q.append(i + j)
    elif com == "TIMES":
        i = q.pop()
        j = q.pop()
        q.append(i * j)
    elif com == "IFZERO":
        i = q.pop()
        if i == 0:
            a = int(x[0])
            continue
    elif com == "DONE":
        print(q.pop())
        break

    a += 1
