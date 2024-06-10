import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

planet = []
for i in range(m):
    sorted_arr = sorted(set(arr[i]))
    mp={}

    for j in range(len(sorted_arr)):
        mp[sorted_arr[j]] = j

    a = []
    for x in arr[i]:
        a.append(mp[x])

    planet.append(a)


ans = 0
for i in range(m):
    for j in range(i, m):
        if i == j:
            continue

        if planet[i] == planet[j]:
            ans += 1


print(ans)
