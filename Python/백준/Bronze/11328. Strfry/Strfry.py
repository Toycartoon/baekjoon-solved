import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = [0 for _ in range(26)]
    s1, s2 = input().split()

    for j in s1:
        a[ord(j)-97] += 1

    for j in s2:
        a[ord(j)-97] -= 1

    ans = 0
    for j in a:
        ans += abs(j)

    if ans != 0:
        print("Impossible")
    else:
        print("Possible")
