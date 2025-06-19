n = int(input())
r = []
for i in range(n):
    r.append(input())

for t in range(int(input())):
    m = int(input())
    if 0 < m <= n:
        print(f"Rule {m}: {r[m-1]}")
    else:
        print(f"Rule {m}: No such rule")
