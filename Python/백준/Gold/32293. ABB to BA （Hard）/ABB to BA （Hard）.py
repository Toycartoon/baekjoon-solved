import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().strip()

    q = []
    b = []
    for i in range(n):
        q.append(s[i])
        while len(q) >= 3 and "".join(q[-3:]) == "ABB":
            for _ in range(3):
                q.pop()
            q.append("B")
            b.append("A")

        q.extend(b)
        b.clear()

    print("".join(q))