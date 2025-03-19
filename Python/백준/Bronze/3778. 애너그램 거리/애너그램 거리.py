import sys

input = sys.stdin.readline

for n in range(int(input())):
    a = input().strip()
    b = input().strip()

    w = [0 for _ in range(26)]
    for i in a:
        w[ord(i)-97] += 1

    for i in b:
        w[ord(i)-97] -= 1

    ans = 0
    for x in w:
        ans += abs(x)

    print(f"Case #{n+1}: {ans}")
