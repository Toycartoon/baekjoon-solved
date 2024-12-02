n = int(input())
s = input()
q = int(input())
for i in range(q):
    l, r = map(int, input().split())

    new_s = s[l-1:r]
    ans = 0

    for j in range(1, len(new_s)):
        x = 0
        for k in range(min(len(new_s[:j]), len(new_s[j:]))):
            if new_s[:j][::-1][k] == new_s[j:][k]:
                x += 1

        ans = max(ans, x)

    print(ans)
