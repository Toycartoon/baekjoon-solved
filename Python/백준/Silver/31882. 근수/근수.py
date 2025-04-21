n = int(input())
s = input() + " "

ans = 0
x = 0
for i in s:
    if i == "2":
        x += 1
    else:
        for v in range(x, 0, -1):
            ans += v * (x-v+1)
        x = 0

print(ans)
