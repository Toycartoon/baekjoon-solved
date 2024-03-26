a, b = map(int, input().split())

ans = 0
l = [True for i in range(int(b ** 0.5)+1)]
l[0] = False
l[1] = False

for i in range(len(l)):
    if l[i]:
        j = 2
        while i ** j <= b:
            if a <= i ** j <= b:
                ans += 1
            j += 1

        for j in range(i * 2, len(l), i):
            l[j] = False


print(ans)
