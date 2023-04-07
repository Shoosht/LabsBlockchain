import hashlib

str = 'Message'

result = hashlib.sha256(str.encode())

print('SHA256 encoded string =',result.hexdigest())