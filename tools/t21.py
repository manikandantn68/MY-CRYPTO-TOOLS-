def generator(g, x, p):
    return pow(g, x, p)

def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        cipher_text += chr(ord(char) ^ ord(key_char))
    return cipher_text

# Parameters
p = 97
g = 31
a = 94
b = 21
cipher = [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]

# Key generation
v = generator(g, b, p)
key = generator(v, a, p)

# Decryption
decipher = ''.join([chr(c // 311 // key) if c != 0 else ' ' for c in cipher])

# XOR encryption
final = dynamic_xor_encrypt(decipher, "aedurtu")
print("picoCTF{" + final + "}")

