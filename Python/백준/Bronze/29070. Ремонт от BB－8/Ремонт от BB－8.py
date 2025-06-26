from math import ceil

a, b, h, w = map(int, input().split())
print(ceil(h / a) * ceil(w / b))
