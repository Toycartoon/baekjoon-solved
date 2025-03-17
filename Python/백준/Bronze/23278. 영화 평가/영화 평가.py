n, l, h = map(int, input().split())
a = list(map(int, input().split()))

print(sum(sorted(a)[l:n-h]) / (n - l - h))