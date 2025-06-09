n = int(input())
a = list(map(int, input().split()))

o, e = 0, 0
for i in a:
    if i % 2 == 0:
        e += 1
    else:
        o += 1

f = True
for i in range(n):
    if i % 2 == 0:
        if o > 0:
            o -= 1
        else:
            f = False
            break
    else:
        if e > 0:
            e -= 1
        else:
            f = False
            break

print(int(f and not o and not e))
