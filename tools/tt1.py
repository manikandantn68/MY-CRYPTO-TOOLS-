from pwn import xor

encrypted_bytes = b"label"
key_integer = 13

xor_result = xor(encrypted_bytes, key_integer).decode()
print(xor_result)
