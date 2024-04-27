m = {0: 0, 1: 1}

def f(n):
    if n in m:
        return m[n]
    m[n] = f(n - 1) + f(n - 2)
    return m[n]

print(f(int(input())))