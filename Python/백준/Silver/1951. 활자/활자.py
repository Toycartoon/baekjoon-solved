n = int(input())
ans = 0

for i in range(1, len(str(n))+1):
    if i == len(str(n)):
        ans += (n - (10 ** (i-1)) + 1) * i
    else:
        ans += int("9" + "0" * (i-1)) * i

print(ans % 1234567)
