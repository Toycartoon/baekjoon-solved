n = int(input())
s = input()
ans = 1

w = {"A": 0, "G": 0, "C": 0, "T": 0}
for i in s:
    w[i] += 1

for i in w:
    ans *= w[i]
    ans %= 1000000007

print(ans)
