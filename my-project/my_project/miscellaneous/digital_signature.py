import nacl.encoding
import nacl.signing

#Generate a new key-pair for bob

bobs_private_key= nacl.signing.SigningKey.generate()
bobs_public_key= bobs_private_key.verify_key


#Bytes to readable format
bobs_public_key_hex= bobs_public_key.encode(encoder=nacl.encoding.HexEncoder)
#print(bobs_public_key_hex)
signed= bobs_private_key.sign(b"Send $37 to Alice")
#print(signed)


#Verifying digital signature
verify_key= nacl.signing.VerifyKey(bobs_public_key_hex,encoder=nacl.encoding.HexEncoder)

decrypted_message=verify_key.verify(signed)
print(decrypted_message)