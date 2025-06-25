br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

b = max(abs(jr-br), abs(jc-bc))
d = abs(jr-dr) + abs(jc-dc)

if d < b:
    print("daisy")
elif b < d:
    print("bessie")
else:
    print("tie")
