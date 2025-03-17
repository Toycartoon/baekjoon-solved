import hashlib

sha = hashlib.sha384()
sha.update(input().encode())
print(sha.hexdigest())