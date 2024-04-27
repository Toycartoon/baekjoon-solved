c = [str(i) for i in range(1, 21)]

for i in range(10):
    s, e = map(int, input().split())

    c[s-1:e] = list(reversed(c[s-1:e]))

print(" ".join(c))