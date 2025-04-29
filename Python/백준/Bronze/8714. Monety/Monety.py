n = int(input())
a = list(map(int, input().split()))
print(min(a.count(1), a.count(0)))