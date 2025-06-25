import sys

input = sys.stdin.readline

ans = 0
while True:
    try:
        e = input().strip().split(".")
        ans += int(e[0]+e[1])
    except IndexError:
        break

print(f"{int(ans) // 100}.{int(ans) % 100:02}")
