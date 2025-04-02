t = input()

i = 1
while True:
    ans = ""
    for x in t:
        ans += chr(ord(x) ^ i)

    if ans.startswith("CHICKENS"):
        print(ans)
        break
    i += 1
