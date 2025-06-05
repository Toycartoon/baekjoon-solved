ans = 0

n = int(input())
for i in range(n):
    s, a, t, m = map(float, input().split())
    ans += (s * (1 + (1 / a)) * (1 + (m / t))) / 4

l = [ans]
p = int(input())
for i in range(p):
    l.append(float(input()))

s = "Younghoon"

l.sort(reverse=True)
if (l.index(ans) + 1) / (p + 1) * 100 <= 15:
    s += " \"The God\""

print(f"The total score of {s} is {ans:.02f}.")
