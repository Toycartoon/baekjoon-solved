n, k = map(int, input().split())
a = list(map(int, input().split()))

w = 0
s = []
for i in a:
    w += i
    s.append(w)

s.sort(reverse=True)
print(sum(s[:k]))