import collections

a, b = map(int, input().split())

matrix = []
vertex = []
q = collections.deque([])
max = -1

for i in range(b):
    vert = []
    for j in range(a):
        vert.append(0)
    vertex.append(vert)
 
for i in range(b):
    temp = list(map(int, input().split()))
    matrix.append(temp)

for i in range(b):
    for j in range(a):
        if matrix[i][j] == 1:
            q.append([i, j, 0])

def ripe(x, y, cnt):
    if x < 0 or x >= b:
        return
    if y < 0 or y >= a:
        return
    if vertex[x][y] == 1:
        return
    if matrix[x][y] == -1 or matrix[x][y] == 1:
        return
    q.append([x, y, cnt+1])
    vertex[x][y] = 1
    matrix[x][y] = 1
    return

while q:
    value = q.popleft()
    x = value[0]
    y = value[1]
    cnt = value[2]

    if cnt > max:
        max = cnt

    ripe(x-1, y, cnt)
    ripe(x+1, y, cnt)
    ripe(x, y+1, cnt)
    ripe(x, y-1, cnt)

result =0
for i in range(b):
    for j in range(a):
        if matrix[i][j] == 0:
            result = 1
            break


if result:
    print(-1)
else:
    print(max)