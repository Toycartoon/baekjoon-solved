n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())

a = 0
for _ in range(m):
    if input() in s:
        a += 1

print(a)