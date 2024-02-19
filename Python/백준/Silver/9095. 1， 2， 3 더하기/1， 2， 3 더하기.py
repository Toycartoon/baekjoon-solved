m = {1: 1, 2: 2, 3: 4}

def add(n):
    if n in m:
        return m[n]
    v1 = add(n - 1)
    v2 = add(n - 2)
    v3 = add(n - 3)
    m[n] = v1 + v2 + v3
    return m[n]

for _ in range(int(input())):
    print(add(int(input())))