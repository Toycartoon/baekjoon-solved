n = int(input())
ans = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        ans.append("DeadMan")
    elif i % 3 == 0:
        ans.append("Dead")
    elif i % 5 == 0:
        ans.append("Man")
    else:
        ans.append(i)


for i in ans:
    print(i, end=" ")
    if str(i).isalpha():
        print()
