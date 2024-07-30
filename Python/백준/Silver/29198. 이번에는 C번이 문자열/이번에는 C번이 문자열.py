n, m, k = map(int, input().split())
w = []
for i in range(n):
    w.append(input())

w.sort()
a = list("".join(w[:k]))
print("".join(sorted(a)))