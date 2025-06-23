n = int(input())
v = int(input())
a = list(map(int, input().split()))

a.append(v)
a.sort(reverse=True)

print(a.index(v)+1)
