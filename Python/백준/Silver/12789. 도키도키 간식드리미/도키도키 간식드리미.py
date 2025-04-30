n = int(input())
a = list(map(int, input().split()))

x = 1
q = []
for i in a:
    if i == x:
        x += 1
    else:
        while len(q):
            v = q.pop()
            if v == x:
                x += 1
            else:
                q.append(v)
                q.append(i)
                break
        else:
            q.append(i)

if q == list(range(n, x-1, -1)):
    print("Nice")
else:
    print("Sad")
