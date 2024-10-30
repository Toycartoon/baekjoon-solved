p = 15000
fibo = [0 for _ in range(p+1)]
fibo[1] = 1

for i in range(2, len(fibo)):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 10000


while True:
    n = int(input())
    if n == -1:
        break
    
    print(fibo[n%p])