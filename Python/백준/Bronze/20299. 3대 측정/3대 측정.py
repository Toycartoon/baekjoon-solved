import sys

input = sys.stdin.readline

n, k, l = map(int, input().split())

ans = []
for i in range(n):
    x1, x2, x3 = map(int, input().split())

    if x1 >= l and x2 >= l and x3 >= l and x1 + x2 + x3 >= k:
        ans.append(f"{x1} {x2} {x3}")


print(len(ans))
print(*ans)
