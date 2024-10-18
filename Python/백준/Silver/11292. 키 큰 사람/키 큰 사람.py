while True:
    n = int(input())
    l = []
    if n == 0:
        break
    
    for i in range(n):
        s, h = input().split()
        l.append((s, float(h)))
    
    l.sort(key=lambda x: x[1], reverse=True)
    mh = l[0][1]
    
    for i in l:
        if mh == i[1]:
            print(i[0], end=" ")
