from math import factorial as f

n = int(input())
print(f(n) // (2 ** (n // 2)) // f(n // 2))
