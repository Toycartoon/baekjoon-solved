w = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()

ans = []
for i in range(len(a)):
    ans.append(w[ord(a[i])-65])
    ans.append(w[ord(b[i])-65])

while len(ans) > 2:
    new_ans = []

    for i in range(1, len(ans)):
        new_ans.append((ans[i] + ans[i-1]) % 10)

    ans = new_ans

for i in ans:
    print(i, end="")
