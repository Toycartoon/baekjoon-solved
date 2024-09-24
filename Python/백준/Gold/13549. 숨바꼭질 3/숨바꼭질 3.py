import heapq


n, k = map(int, input().split())
visited = [False for _ in range(100001)]
q = []

def bfs(n, k):
    visited[n] = True
    heapq.heappush(q, (0, n))

    while q:
        t, x = heapq.heappop(q)

        if x == k:
            print(t)
            break

        if x * 2 <= 100000:
            if not visited[x * 2]:
                visited[x * 2] = True
                heapq.heappush(q, (t, x*2))
        if x + 1 <= 100000 and not visited[x+1]:
            visited[x+1] = True
            heapq.heappush(q, (t+1, x+1))
        if x - 1 >= 0 and not visited[x-1]:
            visited[x-1] = True
            heapq.heappush(q, (t+1, x-1))


bfs(n, k)
