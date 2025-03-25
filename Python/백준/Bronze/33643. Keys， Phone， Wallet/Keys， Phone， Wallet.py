ans = {"phone", "keys", "wallet"}

for n in range(int(input())):
    ans = ans - {input()}

if len(ans) == 0:
    print("ready")
else:
    for i in sorted(list(ans)):
        print(i)
