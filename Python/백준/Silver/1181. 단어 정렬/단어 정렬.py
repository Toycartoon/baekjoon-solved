import sys

w = []
for _ in range(int(sys.stdin.readline())):
    w.append(sys.stdin.readline().rstrip())

w = sorted(list(set(w)))
w.sort(key=len)

for i in w:
    print(i)