import math


def check(v, c):
    s = [v]

    try:
        for com in c:
            if com.startswith("NUM"):
                s.append(int(com.split()[1]))
            elif com == "POP":
                s.pop()
            elif com == "INV":
                s.append(-s.pop())
            elif com == "DUP":
                s.append(s[len(s) - 1])
            elif com == "SWP":
                n1 = s.pop()
                n2 = s.pop()
                s.extend([n1, n2])
            elif com == "ADD":
                n1 = s.pop()
                n2 = s.pop()
                d = n1 + n2
                if abs(d) > 10 ** 9:
                    raise ValueError
                s.append(d)
            elif com == "SUB":
                n1 = s.pop()
                n2 = s.pop()
                d = n2 - n1
                if abs(d) > 10 ** 9:
                    raise ValueError
                s.append(d)
            elif com == "MUL":
                n1 = s.pop()
                n2 = s.pop()
                d = n1 * n2
                if abs(d) > 10 ** 9:
                    raise ValueError
                s.append(d)
            elif com == "DIV":
                n1 = s.pop()
                n2 = s.pop()
                s.append(math.trunc(n2 / n1))
            elif com == "MOD":
                n1 = s.pop()
                n2 = s.pop()
                if n2 < 0:
                    s.append(-(abs(n2) % abs(n1)))
                else:
                    s.append(abs(n2) % abs(n1))

        if len(s) != 1:
            return "ERROR"
        else:
            return s[0]
    except:
        return "ERROR"


c = []
while True:

    c_ = input()

    if c_ == "QUIT":
        break
    elif c_ == "END":
        n = int(input())

        for _ in range(n):
            v = int(input())
            print(check(v, c))
        print()
        c = []
    else:
        c.append(c_)
