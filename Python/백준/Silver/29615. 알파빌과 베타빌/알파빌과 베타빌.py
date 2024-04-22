n, m = map(int, input().split())
ln = list(map(int, input().split()))
lm = set(map(int, input().split()))

a = 0
for i in range(m):
    if ln[i] not in lm:
        a += 1

print(a)