# Baekjoon 10828

import sys

n = int(sys.stdin.readline())

s = []
for _ in range(n):
    com = sys.stdin.readline()
    if 'push' in com:
        s.append(int(com.split()[1]))
    elif 'pop' in com:
        try:
            sys.stdout.write(str(s.pop()) + "\n")
        except IndexError:
            sys.stdout.write("-1\n")
    elif 'size' in com:
        sys.stdout.write(str(len(s)) + "\n")
    elif 'empty' in com:
        if len(s) == 0:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    else:
        try:
            sys.stdout.write(str(s[len(s) - 1]) + "\n")
        except IndexError:
            sys.stdout.write("-1\n")