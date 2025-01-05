import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
a = list(map(int, input().split()))

ans = a[:l-1] + sorted(a[l-1:r]) + a[r:]
print(int(ans == sorted(a)))