import hashlib

input_bytes =b'I love you tatchom laurence'
output =hashlib.sha256(input_bytes)

print(output.hexdigest())