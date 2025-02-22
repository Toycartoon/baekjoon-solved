a, b = map(int, input().split())
print(abs((b - 1) // 4 - (a - 1) // 4) + abs((b % 4 if b % 4 != 0 else 4) - (a % 4 if a % 4 != 0 else 4)))