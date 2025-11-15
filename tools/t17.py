def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - ord('A')
            encrypted_char = chr((ord(char) - offset + key_shift) % 26 + offset)
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char  # Keep non-alphabet characters unchanged
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - offset - key_shift) % 26 + offset)
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char  # Keep non-alphabet characters unchanged
    return plaintext

# Example usage
cipher_text = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"
key = "CYLAB"  # Replace with the actual key

decrypted = vigenere_decrypt(cipher_text, key)
print("Decrypted:", decrypted)

