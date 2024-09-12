# Special Thanks: lighter

from math import sqrt, pi
from decimal import Decimal as d


n = int(input())
p = []

ans = 0

if n <= 2:
    print(0)
    exit()

for i in range(n):
    x, y = map(int, input().split())

    p.append((x, y))


p.append(p[0])

ratio = 0
l = sqrt((d(f"{p[1][0]}") - d(f"{p[0][0]}")) ** d("2.0") + (d(f"{p[1][1]}") - d(f"{p[0][1]}")) ** d("2.0")) # 한 변의 길이
s = d(f"{sqrt(3)}") / d("4.0") * (d(f"{l}") ** d("2.0"))    # 정삼각형의 넓이
r = d(f"{l}") * (d("1.0") / (d("2.0") * d(f"{sqrt(3)}")))   # 내접원의 반지름
a = (s - (d(f"{pi}") * r ** d("2.0"))) / 3  # 내접원의 넓이
ratio = d(f"{a}") / d(f"{s}")           # 정삼각형 : 정삼각형 - 내접원 / 3의 비율


poly_s = 0
for i in range(n):
    poly_s += d(f"{p[i][0]}") * d(f"{p[i+1][1]}")

for i in range(n):
    poly_s -= d(f"{p[i][1]}") * d(f"{p[i+1][0]}")


print(abs(d(f"{poly_s}") / d("2.0")) * ratio)
