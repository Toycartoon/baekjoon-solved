n = int(input())
a = list(map(int, input().split()))

s = []
for i in a:
    if 0 <= i <= 4:
        s.append(i)

print(sum(s) / len(s))
