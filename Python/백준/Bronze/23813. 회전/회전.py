n = list(map(int, [*input()]))
ans = 0
for i in range(len(n)):
    n.insert(0, n.pop())
    temp = ""
    for x in n:
        temp += str(x)
    ans += int(temp)

print(ans)
