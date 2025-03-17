import base64

s = input().encode()
ans = base64.b64decode(s)
print(ans.decode())
