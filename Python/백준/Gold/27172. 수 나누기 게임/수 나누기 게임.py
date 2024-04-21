import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
l = list(map(int, input().split()))

ans = [0 for _ in range(n)]

record_idx = {}
temp = set()
for i in range(n):
    record_idx[l[i]] = i
    temp.add(l[i])
l.sort()

m_num = max(l)
for i in range(n):
    t = l[i]
    for j in range(t * 2, m_num + 1, t):
        if j in temp:
            ans[record_idx[t]] += 1
            ans[record_idx[j]] -= 1

for i in ans:
    print(str(i) + " ")
