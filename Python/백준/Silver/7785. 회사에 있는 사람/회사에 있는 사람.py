import sys

s = set()
for _ in range(int(input())):
    p, l = sys.stdin.readline().rstrip().split()
    if l == "enter":
        s.add(p)
    else:
        s.remove(p)

for i in sorted(list(s), reverse=True):
    sys.stdout.write(f"{i}\n")