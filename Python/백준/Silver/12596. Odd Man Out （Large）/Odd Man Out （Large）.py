for t in range(int(input())):
    n = int(input())
    s = set()
    a = list(map(int, input().split()))

    for i in a:
        if i in s:
            s.remove(i)
        else:
            s.add(i)

    print(f"Case #{t+1}:", s.pop())
