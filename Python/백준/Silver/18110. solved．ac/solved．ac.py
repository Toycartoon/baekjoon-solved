import sys

input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

l.sort()
c = round(n * (15 / 100) + 10 ** -5)

print(round(sum(l[c:n-c]) / (n - (2 * c)) + 10 ** -5) if n != 0 else 0)