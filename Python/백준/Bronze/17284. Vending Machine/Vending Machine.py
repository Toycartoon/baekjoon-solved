ans = 5000
for i in list(map(int, input().split())):
    if i == 1:
        ans -= 500
    elif i == 2:
        ans -= 800
    elif i == 3:
        ans -= 1000

print(ans)
