import sys

input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    i = 2
    while True:
        k = i * (i - 1) // 2

        if i + k > n:
            print("IMPOSSIBLE\n")
            break
        if (n - k) % i == 0:
            a = (n - k) // i
            print(f"{n} = ")
            for j in range(i-1):
                print(str(a + j) + " + ")
            print(str(a + (i-1)) + "\n")
            break

        i += 1