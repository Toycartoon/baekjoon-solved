n = input()
if sum(map(int, [*n[:len(n)//2]])) == sum(map(int, [*n[len(n)//2:]])):
    print("LUCKY")
else:
    print("READY")
