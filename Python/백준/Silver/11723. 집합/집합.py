import sys

print = sys.stdout.write

s = set()
for _ in range(int(input())):
    c, *n = sys.stdin.readline().rstrip().split()
    if c == "all":
        s = set(i for i in range(1, 21))
    elif c == "empty":
        s = set()
    elif c == "add":
        s.add(int(n[0]))
    elif c == "remove":
        if int(n[0]) in s:
            s.remove(int(n[0]))
    elif c == "check":
        if int(n[0]) in s:
            print("1\n")
        else:
            print("0\n")
    else:
        if int(n[0]) in s:
            s.remove(int(n[0]))
        else:
            s.add(int(n[0]))