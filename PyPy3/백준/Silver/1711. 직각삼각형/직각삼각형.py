import sys

input = sys.stdin.readline

p = []
for i in range(int(input())):
    x, y = map(int, input().split())
    p.append((x, y))

ans = 0
for i in range(len(p)):
    for j in range(i+1, len(p)):
        for k in range(j+1, len(p)):
            a, b, c = p[i], p[j], p[k]

            ax, ay = a
            bx, by = b
            cx, cy = c

            ab = (ax - bx) ** 2 + (ay - by) ** 2
            bc = (bx - cx) ** 2 + (by - cy) ** 2
            ac = (ax - cx) ** 2 + (ay - cy) ** 2

            mx = max(ab, bc, ac)
            if (mx == ab and ab == bc + ac) or (mx == bc and bc == ab + ac) or (mx == ac and ac == ab + bc):
                ans += 1


print(ans)
