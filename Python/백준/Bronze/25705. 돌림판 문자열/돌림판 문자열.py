from queue import Queue

n = int(input())
d = input()
m = int(input())
s = input()

if {*s} - {*d} != set():
    print(-1)
    exit()

q = Queue()
for i in d:
    q.put(i)

ans = 0
p = 0
while p < m:
    x = q.get()
    if x == s[p]:
        p += 1
    q.put(x)
    ans += 1

print(ans)