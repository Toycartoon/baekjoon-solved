n = int(input())
s = input().split("0")

ans = 0
for i in s:
    ans += sum(range(len(i), 0, -1))

print(ans)
