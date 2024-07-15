n = int(input())
x = []
for _ in range(n):
    a, b = map(int, input().split())

    x.append(b)

print(abs(max(x) - min(x)))
