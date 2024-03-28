from sys import stdin, stdout

t = int(stdin.readline())

for _ in range(t):
    p = stdin.readline().split("\n")[0]
    n = int(stdin.readline())
    x = stdin.readline().split("\n")[0]
    x = x[1:len(x) - 1].split(",")
    d = 0
    r = 0

    for i in range(n):
        x[i] = int(x[i])

    l = True
    for f in p:
        if f == "R":
            r += 1
            if d == 0:
                d = len(x) - 1
            else:
                d = 0
        else:
            if x == ['']:
                stdout.write("error\n")
                l = not l
                break
            try:
                x.pop(d)
                if d != 0:
                    d = len(x) - 1
            except IndexError:
                stdout.write("error\n")
                l = not l
                break
    if l:
        if r % 2 == 1:
            x.reverse()
        stdout.write("[" + ",".join(str(a) for a in x) + "]\n")
