import base64

s = input().encode()
ans = base64.b64encode(s)
print(ans.decode())
