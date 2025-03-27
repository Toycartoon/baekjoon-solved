m, n = map(int, input().split())
w = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "night"]

a = []
for i in range(m, n+1):
    s = ''
    for x in str(i):
        s += w[int(x)]

    a.append((s, i))

a.sort()
for i in range(10, len(a)+10, 10):
    [print(x[1], end=' ') for x in a[i-10:i]]
    print()
