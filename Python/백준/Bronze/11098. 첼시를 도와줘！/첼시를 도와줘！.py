for t in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        p = input().split()
        l.append((int(p[0]), p[1]))
    
    l.sort(key=lambda x: x[0], reverse=True)
    print(l[0][1])
