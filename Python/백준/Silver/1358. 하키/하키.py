import sys

input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())

ans = 0
for i in range(p):
    xi, yi = map(int, input().split())

    if x <= xi <= x + w and y <= yi <= y + h:
        ans += 1
    else:
        r = h // 2

        if x - r <= xi <= x and y <= yi <= y + h:
            c = ((xi - x) ** 2 + (yi - (y + r)) ** 2) ** 0.5

            if c <= r:
                ans += 1
        elif x + w + r >= xi >= x + w and y <= yi <= y + h:
            c = ((xi - (x + w)) ** 2 + (yi - (y + r)) ** 2) ** 0.5

            if c <= r:
                ans += 1


print(ans)
