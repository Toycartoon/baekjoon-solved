import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    ans = 0
    x = 0
    l = list(map(int, input().split()))
    c = [0 for _ in range(max(l)+1)]

    for i in l:
        c[i] += 1

    set_m = False
    m = len(c)-1
    for i in range(n-1):
        if not set_m:
            for a in range(m, -1, -1):
                if c[a] != 0:
                    m = a
                    set_m = True
                    break

        if l[i] != m:
            x += 1
            ans += (l[i+1] - l[i]) * x
        else:
            x = 0
            ans += (l[i+1] - l[i]) * x
            set_m = False

        c[l[i]] -= 1

    print(ans)
