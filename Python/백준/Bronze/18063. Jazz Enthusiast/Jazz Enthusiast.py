n, c = map(int, input().split())
ans = 0

t = 0
for i in range(n):
    m, s = map(int, input().split(":"))

    if i >= 1:
        s -= c

    t += m * 60 + s

min = t // 60
sec = t % 60

hour = min // 60
min = min % 60

print(f"{hour:02}:{min:02}:{sec:02}")
