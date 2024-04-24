for n in range(1, int(input())+1):
    s = set()
    c = int(input())
    for g in input().split():
        if g in s:
            s.remove(g)
        else:
            s.add(g)
    print(f"Case #{n}: {s.pop()}")