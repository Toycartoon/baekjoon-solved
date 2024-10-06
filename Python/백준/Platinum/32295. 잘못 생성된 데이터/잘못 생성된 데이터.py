for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    if 475 < l.index(1) < 525:
        print("Bob", flush=True)
    else:
        print("Alice", flush=True)
