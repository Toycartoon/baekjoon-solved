k, n = map(int, input().split())
a = (n * k) // (n - 1) if n != 1 else -1
if a != -1 and (n * k) % (n - 1) != 0:
    a += 1

print(a)
