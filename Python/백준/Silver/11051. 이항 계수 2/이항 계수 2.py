import math

n, k = map(int, input().split())

print(int(math.factorial(n)) // int(math.factorial(k) * math.factorial(n - k)) % 10007)
