s, l = set(), set()
n, m = map(int, input().split())

for _ in range(n):
    s.add(input())
for _ in range(m):
    l.add(input())

sl = s & l
sl = sorted(sl)
print(len(sl))
for i in sl:
    print(i)