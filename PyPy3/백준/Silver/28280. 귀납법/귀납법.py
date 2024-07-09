from collections import deque

def bfs(k):
    visited = [False] * ((4 * 10 ** 6) + 1)
    q = deque()

    visited[1] = True
    q.append((1, 0))

    while q:
        x, v = q.popleft()

        if x == k:
            return v
        if x - 1 > 0:
            if not visited[x - 1]:
                visited[x - 1] = True
                q.append((x-1, v+1))
        if x * 2 <= 4 * 10 ** 6:
            if not visited[x * 2]:
                visited[x * 2] = True
                q.append((x*2, v+1))

    return -1


for t in range(int(input())):
    k = int(input())

    r = bfs(k)
    if r == -1:
        print("Wrong proof!")
    else:
        print(r)
