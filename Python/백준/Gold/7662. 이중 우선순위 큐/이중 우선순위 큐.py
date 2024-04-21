import heapq, sys

input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    minq = []
    maxq = []
    k = int(input())
    visited = [False] * k
    idx = 0
    for __ in range(k):
        c, n = input().split()
        if c == "I":
            heapq.heappush(minq, (int(n), idx))
            heapq.heappush(maxq, (-int(n), idx))
            idx += 1
        else:
            try:
                if n == "-1":
                    while True:
                        a, i = heapq.heappop(minq)
                        if not visited[i]:
                            break
                    visited[i] = True
                else:
                    while True:
                        a, i = heapq.heappop(maxq)
                        if not visited[i]:
                            break
                    visited[i] = True
            except:
                pass

    ans = []
    for i in minq:
        if not visited[i[1]]:
            ans.append(i[0])

    if len(ans) == 0:
        print("EMPTY\n")
    else:
        print(f"{max(ans)} {min(ans)}\n")