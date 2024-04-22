a, b = map(int, input().split())
x = [a]
y = [b]

n = 0
while True:
    x.append((x[n] + y[n]) / 2)
    y.append(2 * ((x[n] * y[n]) / (x[n] + y[n])))

    if x[n - 1] == x[n] and y[n - 1] == y[n]:
        break
    n += 1

print("{:.6f} {:.6f}".format(x[n], y[n]))