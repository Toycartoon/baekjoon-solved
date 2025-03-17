import base64

s = input().encode()
ans = base64.b32encode(s)
print(ans.decode())
