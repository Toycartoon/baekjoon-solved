n = int(input())
s = set()

for i in range(n):
    s.add(input())

ans = 0
for x in range(int(input())):
    i = input()

    if i in s:
        ans += 1

print(ans)
