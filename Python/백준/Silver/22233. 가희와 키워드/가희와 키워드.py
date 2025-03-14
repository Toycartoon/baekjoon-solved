import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = set()
for i in range(n):
    k.add(input().strip())

for i in range(m):
    x = {*input().strip().split(",")}
    k -= x

    print(len(k))
