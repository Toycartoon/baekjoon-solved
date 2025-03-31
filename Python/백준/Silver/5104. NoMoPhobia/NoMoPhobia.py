import sys

input = sys.stdin.readline

p = {"TT": 75, "TX": 50, "PR": 80, "RT": 30, "AP": 25, "PX": 60}
while True:
    w, n = map(int, input().split())

    if w == n == 0:
        break

    x = {}
    for i in range(n):
        s, c = input().strip().split()

        if s not in x:
            x[s] = p[c]
        else:
            x[s] += p[c]

    print(f"Week {w} ", end="")
    ans = []
    for i in x:
        if x[i] >= 100:
            ans.append(i)

    if len(ans) == 0:
        print("No phones confiscated")
    else:
        print(",".join(ans))
