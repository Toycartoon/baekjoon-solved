import sys

input = sys.stdin.readline

l = [0] * 1001
ans = 0
jinju = 0
for n in range(int(input())):
    d, c = input().split()

    if d == "jinju":
        jinju = int(c)
    else:
        if int(c) <= 1000 and jinju == 0:
            l[int(c)] += 1
        else:
            if jinju < int(c):
                ans += 1

for i in range(len(l)):
    if i > jinju:
        ans += l[i]

print(jinju)
print(ans)
