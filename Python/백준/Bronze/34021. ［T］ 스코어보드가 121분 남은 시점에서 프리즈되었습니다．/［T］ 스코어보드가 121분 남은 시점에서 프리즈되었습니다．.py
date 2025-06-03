for t in range(int(input())):
    n, m, l = map(int, input().split())
    s = list(map(int, input().split()))

    ans = [l]
    for i in s:
        if i == -1:
            continue
        ans.append(m - i)

    print(f"The scoreboard has been frozen with {str(max(ans)) + ' minutes' if max(ans) != 1 else '1 minute'} remaining.")
