import base64

s = input().encode()
ans = base64.b32decode(s)
print(ans.decode())
