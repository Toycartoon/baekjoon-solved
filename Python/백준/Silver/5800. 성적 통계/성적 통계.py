for x in range(1, int(input())+1):
    k, *n = map(int, input().split())
    g = -1
    n.sort()
    for i in range(1, k):
        if g < n[i] - n[i-1]:
            g = n[i] - n[i-1]
    print(f"Class {x}")
    print(f"Max {max(n)}, Min {min(n)}, Largest gap {g}")
