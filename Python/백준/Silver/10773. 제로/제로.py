k = int(input())

cog = []
for _ in range(k):
    called = int(input())
    if called == 0:
        cog.pop()
    else:
        cog.append(called)

total = 0
for i in cog:
    total += i

print(total)