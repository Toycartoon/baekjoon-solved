import sys

input = sys.stdin.readline
print = sys.stdout.write

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

ps = []
s = 0
for i in a:
    s += i
    ps.append(s)

for _ in range(q):
    l, r = map(int, input().split())
    if l == 1:
        print(f"{ps[r-1]}\n")
    else:
        print(f"{ps[r-1] - ps[l-2]}\n")
