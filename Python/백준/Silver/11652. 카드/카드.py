import sys, heapq

input = sys.stdin.readline

q = []
s = {}
for i in range(int(input())):
    n = int(input())

    if n not in s:
        s[n] = 1
    else:
        s[n] += 1


for i in s.keys():
    heapq.heappush(q, (-s[i], i))

print(heapq.heappop(q)[1])
