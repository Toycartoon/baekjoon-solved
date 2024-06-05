k = int(input())
menu = list(map(int, input().split()))
x = int(input())
set_menu = list(map(int, input().split()))
t = int(input())
order = list(map(int, input().split()))

sum = [0] * (k + 1)
for i in order:
    sum[i] += 1

ans = 0
for i in order:
    if sum[i] <= 0:
        continue

    if i not in set_menu:
        ans += menu[i-1]
        sum[i] -= 1
    else:
        need = []
        for j in range(len(sum)):
            if sum[j] > 0 and j in set_menu and j not in need:
                need.append(j)

        full_cost = 0
        for cost in need:
            full_cost += menu[cost-1]
            sum[cost] -= 1

        if full_cost < x:
            ans += full_cost
        else:
            ans += x

print(ans)
