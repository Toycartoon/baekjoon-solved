from collections import deque


for t in range(int(input())):
    n, m = map(int, input().split())
    x = int("".join(input().split()))
    y = int("".join(input().split()))

    num = deque(list(map(int, input().split())))

    ans = 0
    for i in range(n):
        z = ""
        for j in range(m):
            z += str(num[j])
        if x <= int(z) <= y:
            ans += 1
        num.rotate(1)

    print(ans)
