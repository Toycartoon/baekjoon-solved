arr = [i for i in range(2000000)]
arr[1] = 0

for i in range(2, int(2000000 ** 0.5)):
    if arr[i] == 0:
        continue

    for j in range(i * i, 2000000, i):
        arr[j] = 0


n = int(input())
for i in range(2000000):
    if arr[i] >= n and str(arr[i]) == str(arr[i])[::-1]:
        print(arr[i])
        break
