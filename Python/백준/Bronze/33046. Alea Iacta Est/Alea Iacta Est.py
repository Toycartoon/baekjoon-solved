a, b = map(int, input().split())
c, d = map(int, input().split())

s = a + b + c + d - 1
print(s % 4 if s % 4 != 0 else 4)
