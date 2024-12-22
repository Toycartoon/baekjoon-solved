t, x = map(int, input().split())
f = True

for n in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))

    if x not in a:
        f = False
        break

if f:
    print("YES")
else:
    print("NO")