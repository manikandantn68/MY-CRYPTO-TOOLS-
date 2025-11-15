def otp_decrypt(ciphertext, key):
    plaintext = ""
    for c, k in zip(ciphertext.upper(), key.upper()):
        # Convert letters to numbers: A=0, B=1, ..., Z=25
        c_num = ord(c) - ord('A')
        k_num = ord(k) - ord('A')
        # Decrypt: (cipher - key) mod 26
        p_num = (c_num - k_num) % 26
        plaintext += chr(p_num + ord('A'))
    return plaintext

# Challenge input
ciphertext = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

# Decrypt
plaintext = otp_decrypt(ciphertext, key)
print("Decrypted message:", plaintext)

