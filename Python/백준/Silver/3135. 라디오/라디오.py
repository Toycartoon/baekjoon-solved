a, b = map(int, input().split())
ans = [abs(b-a)]
for n in range(int(input())):
    i = int(input())
    ans.append(abs(i-b)+1)


print(min(ans))
