from collections import deque


for t in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    sl = sorted(l, reverse=True)
    q = deque(l)

    i = 0
    ans = 1
    while q:
        x = q.popleft()

        if x == sl[i]:
            if m == 0:
                print(ans)
                break
            else:
                ans += 1
                m -= 1
                i += 1
        else:
            q.append(x)
            m -= 1
            if m < 0:
                m = len(q) - 1
