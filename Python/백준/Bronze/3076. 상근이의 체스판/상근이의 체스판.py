r, c = map(int, input().split())
a, b = map(int, input().split())

s = ("X" * b + "." * b) * (c // 2)
if c % 2 == 1:
    s += "X" * b

for x in range(r):
    for i in range(a):
        print(s)
    s = s.replace(".", " ").replace("X", ".").replace(" ", "X")
