import sys

input = sys.stdin.readline

ans = [[] for _ in range(4)]
w = []
n = int(input())
for i in range(n):
    s, d = input().strip().split()
    w.append((s, int(d)))

w.sort(key=lambda x: -x[1])
for i in range(n):
    ans[i % 4].append(w[i][0])

for i in range(4):
    print(i+1, *sorted(ans[i]))
