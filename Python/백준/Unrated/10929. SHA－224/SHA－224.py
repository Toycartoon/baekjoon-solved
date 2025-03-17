import hashlib

sha = hashlib.sha224()
sha.update(input().encode())
print(sha.hexdigest())