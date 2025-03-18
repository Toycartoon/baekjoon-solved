s = [*input()]
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]

print("".join(s))
