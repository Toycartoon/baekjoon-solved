n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l.reverse()
ans = 0
b = l[0]

for i in range(1, n):
    if l[i] < b:
        b = l[i]
    elif l[i] == b:
        ans += 1
        b -= 1
    else:
        ans += abs(b - l[i]) + 1
        b -= 1

print(ans)
