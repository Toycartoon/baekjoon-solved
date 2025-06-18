n = int(input())
x = list(map(int, input().split()))

v = [0 for _ in range(n+1)]
for i in x:
    v[i] += 1

v[0] = 0
print(v.index(max(v)) if v.count(max(v)) == 1 else "skipped")
