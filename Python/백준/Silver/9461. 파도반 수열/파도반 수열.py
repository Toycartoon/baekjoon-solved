m = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}

def f(n):
    if n in m:
        return m[n]
    v = f(n - 1) + f(n - 5)
    m[n] = v

    return m[n]

for _ in range(int(input())):
    print(f(int(input())))