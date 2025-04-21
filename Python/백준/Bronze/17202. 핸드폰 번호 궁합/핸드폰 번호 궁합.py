a = input()
b = input()

ans = []
for i in range(len(a)):
    ans.append(int(a[i]))
    ans.append(int(b[i]))

while len(ans) > 2:
    new_ans = []

    for i in range(1, len(ans)):
        new_ans.append((ans[i] + ans[i-1]) % 10)

    ans = new_ans

for i in ans:
    print(i, end="")
