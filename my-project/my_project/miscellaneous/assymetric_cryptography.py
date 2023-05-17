from nacl.public import PrivateKey, Box
# Generate secret keys for Alice and Bob
alices_private_key = PrivateKey.generate()
bobs_private_key = PrivateKey.generate()
# Public keys are generated from the private keys
alices_public_key = alices_private_key.public_key
bobs_public_key = bobs_private_key.public_key
# Bob will send Alice a message...
# So he makes a Box with his private key and Alice's public key
bobs_box = Box(bobs_private_key, alices_public_key)
# We encrypt Bob's secret message (bytes)...
encrypted = bobs_box.encrypt(b"I am Satoshi")
# Alice creates a second box with her private key and Bob's
#public key so that she can decrypt the message

alices_box = Box(alices_private_key, bobs_public_key)
# Now Alice can decrypt the message:
plaintext = alices_box.decrypt(encrypted)
print(plaintext.decode('utf-8'))