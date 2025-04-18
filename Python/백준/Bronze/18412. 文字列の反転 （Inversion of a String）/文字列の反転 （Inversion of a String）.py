n, a, b = map(int, input().split())
s = [*input()]
s[a-1:b] = reversed(s[a-1:b])
print("".join(s))