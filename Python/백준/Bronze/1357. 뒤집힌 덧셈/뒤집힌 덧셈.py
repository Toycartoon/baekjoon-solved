x, y = map(int, input().split())

print(int(str(int(str(x)[::-1]) + int(str(y)[::-1]))[::-1]))
