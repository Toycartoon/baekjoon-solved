n = int(input())
c = {}
a = list(input().split())

for i in range(n):
    if a[i] not in c:
        c[a[i]] = 1
    else:
        c[a[i]] += 1

    if max(c.values()) > 4:
        print(i+1)
        exit()


print(0)
