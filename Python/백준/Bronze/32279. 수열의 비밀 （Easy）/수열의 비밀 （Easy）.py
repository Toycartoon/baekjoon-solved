n = int(input())
p, q, r, s = map(int, input().split())
a = [int(input())]

for i in range(2, n+1):
    if i % 2 == 0:
        a.append(p * a[i // 2 - 1] + q)
    else:
        a.append(r * a[i // 2 - 1] + s)

print(sum(a))
