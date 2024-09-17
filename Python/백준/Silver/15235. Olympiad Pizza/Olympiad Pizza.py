from queue import Queue

n = int(input())
a = list(map(int, input().split()))

i = 1
get = [0] * n
ans = [0] * n

q = Queue()
for x in range(1, n+1):
    q.put(x)


while not q.empty():
    x = q.get()
    get[x-1] += 1

    if get[x-1] == a[x-1]:
        ans[x-1] = i
    else:
        q.put(x)

    i += 1


print(*ans)
