import sys

x = 0
s = 0
for _ in range(int(sys.stdin.readline())):
    com = list(map(int, sys.stdin.readline().split()))

    if com[0] == 1:
        s += com[1]
        x ^= com[1]
    elif com[0] == 2:
        s -= com[1]
        x ^= com[1]
    elif com[0] == 3:
        sys.stdout.write(str(s) + "\n")
    else:
        sys.stdout.write(str(x) + '\n')