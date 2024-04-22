# Baekjoon 1316

n = int(input())

count = 0

for __ in range(n):
    check = [[0, -1] for _ in range(26)]
    s = input()
    flag = True

    for i in range(len(s)):
        if check[ord(s[i]) - 97][0] >= 1:
            if check[ord(s[i]) - 97][1] != i - 1:
                flag = False
                break
        check[ord(s[i]) - 97][0] += 1
        check[ord(s[i]) - 97][1] = i

    if flag:
        count += 1

print(count)
