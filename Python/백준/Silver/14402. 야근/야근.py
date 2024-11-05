import sys

input = sys.stdin.readline

arr = {}
ans = 0
q = int(input())
for i in range(q):
    s, p = input().split()

    if p == "+":
        if s not in arr:
            arr[s] = 1
        else:
            arr[s] += 1
    elif p == "-":
        if s not in arr:
            ans += 1
        else:
            if arr[s] == 0:
                ans += 1
            else:
                arr[s] -= 1


for i in arr.keys():
    ans += arr[i]


print(ans)
