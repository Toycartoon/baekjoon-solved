n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in enumerate(zip(*g)):
    ans.append((sum(i[1]), i[0]+1))

ans.sort(key=lambda x: (-x[0], x[1]))
print(*[i[1] for i in ans])
