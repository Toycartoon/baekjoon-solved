o1, o2 = 1, 1
n, a, b = map(int, input().split())

for i in range(n):
    o1 += a
    o2 += b
    
    if o1 < o2:
        o1, o2 = o2, o1
    elif o1 == o2:
        o2 -= 1

print(o1, o2)