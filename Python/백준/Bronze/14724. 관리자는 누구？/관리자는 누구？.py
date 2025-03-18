n = int(input())
ans = []

for k in range(9):
    ans.append(max(list(map(int, input().split()))))

print(["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"][ans.index(max(ans))])