l = []

while True:
    try:
        l.extend(list(input().split()))
    except EOFError:
        break

l = l[::-1]
l.pop()

x = []
for i in l:
    x.append(int(i[::-1]))

x.sort()
for i in x:
    print(i)
