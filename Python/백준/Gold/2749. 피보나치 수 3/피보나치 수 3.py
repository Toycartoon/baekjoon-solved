p = 15 * 10 ** 5
fibo = [0 for _ in range(p+1)]
fibo[1] = 1

for i in range(2, len(fibo)):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % (10 ** 6)
    
n = int(input())
print(fibo[n % p])
