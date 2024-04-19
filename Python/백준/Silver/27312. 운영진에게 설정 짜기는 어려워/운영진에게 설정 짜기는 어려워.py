m, n, q = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for k in range(m):
    print(f"? {k+1} {k+1}", flush=True)

    s = int(input())
    ans.append(str(s + 1) if s < a[k] else "1")


if len(ans) < n:
    for i in range(n - len(ans)):
        ans.append("1")

print(f"! {' '.join(ans)}", flush=True)
