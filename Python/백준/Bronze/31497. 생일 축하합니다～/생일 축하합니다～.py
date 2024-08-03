n = int(input())
s = [input() for _ in range(n)]

for i in range(n):
    for x in range(2):
        print(f"? {s[i]}", flush=True)
        ans = int(input())

        if ans == 1:
            print(f"! {s[i]}", flush=True)
            exit()
