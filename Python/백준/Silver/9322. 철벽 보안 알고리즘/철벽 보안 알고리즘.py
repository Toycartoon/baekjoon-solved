for _ in range(int(input())):
    n = int(input())
    v1 = input().split()
    v2 = input().split()
    w = input().split()
    p = {}
    for j in range(n):
        p[v1[j]] = v2.index(v1[j])

    for j in v1:
        print(w[p[j]], end=" ")