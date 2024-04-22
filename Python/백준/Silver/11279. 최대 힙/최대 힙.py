import heapq
import sys

q = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(-heapq.heappop(q)) + "\n")
    else:
        heapq.heappush(q, -x)