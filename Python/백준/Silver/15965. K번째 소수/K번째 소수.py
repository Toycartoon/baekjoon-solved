k = int(input())
arr = [True] * 7368788
arr[0] = False
arr[1] = False

x = 0
for i in range(len(arr)):
    if not arr[i]:
        continue
    else:
        x += 1
        if x == k:
            print(i)
            break

        for j in range(i**2, len(arr), i):
            arr[j] = False
