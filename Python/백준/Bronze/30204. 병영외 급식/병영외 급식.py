n, x = map(int, input().split())
l = list(map(int, input().split()))

print(int(sum(l) % x == 0))