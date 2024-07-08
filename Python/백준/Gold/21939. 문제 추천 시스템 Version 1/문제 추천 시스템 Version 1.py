import sys
import heapq

input = sys.stdin.readline

max_q = []
min_q = []

n = int(input())
visited = [False] * n
idx = 0
bind = {}

for i in range(n):
    p, l = map(int, input().split())

    heapq.heappush(max_q, (-l, -p, idx))
    heapq.heappush(min_q, (l, p, idx))
    bind[p] = idx

    idx += 1

for i in range(int(input())):
    com, v, *w = input().split()

    if com == "recommend":
        if v == "1":
            while True:
                l, p, x = heapq.heappop(max_q)
                if not visited[x]:
                    heapq.heappush(max_q, (l, p, x))
                    break

            print(-p)
        elif v == "-1":
            while True:
                l, p, x = heapq.heappop(min_q)
                if not visited[x]:
                    heapq.heappush(min_q, (l, p, x))
                    break

            print(p)
    if com == "add":
        heapq.heappush(max_q, (-int(w[0]), -int(v), idx))
        heapq.heappush(min_q, (int(w[0]), int(v), idx))

        bind[int(v)] = idx
        visited.append(False)

        idx += 1
    if com == "solved":
        visited[bind[int(v)]] = True
