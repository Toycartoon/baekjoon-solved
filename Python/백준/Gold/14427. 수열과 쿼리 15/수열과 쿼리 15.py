import heapq, sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
q = []
for i in range(1, n+1):
    heapq.heappush(q, (a[i-1], i))

for m in range(int(input())):
    c, *x = map(int, input().split())

    if c == 1:
        a[x[0]-1] = x[1]
        heapq.heappush(q, (x[1], x[0]))
    elif c == 2:
        while True:
            i = heapq.heappop(q)
            if a[i[1]-1] == i[0]:
                print(i[1])
                heapq.heappush(q, i)
                break
