import base58

text = 'Message'
base58Str = base58.b58encode(text.encode('utf-8')).decode('utf-8')
print("Base58 encoded string = " + base58Str)

text = base58.b58decode(base58Str).decode('utf-8')
print("Base58 decoded string = " + text)

