a = int(input())
b = int(input())

print(a)
print(b)
for i in range(len(str(b))-1, -1, -1):
    print(a * int(str(b)[i]))

print(a * b)