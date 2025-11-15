def caesar_decrypt(ciphertext, shift):
    """
    Decrypts a Caesar cipher by shifting letters backward by the given shift value.
    Non-alphabetic characters are left unchanged.
    """
    decrypted = ""
    for char in ciphertext:
        """
        Loop through each character in the ciphertext.
        If it's a letter, shift it backward.
        """
        if char.isalpha():
            """
            Determine if the character is uppercase or lowercase.
            Set the base ASCII value accordingly.
            """
            base = ord('A') if char.isupper() else ord('a')
            """
            Shift the character backward by 'shift' positions.
            Wrap around using modulo 26 to stay within alphabet bounds.
            """
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            """
            If the character is not a letter, keep it as-is.
            """
            decrypted += char
    return decrypted

ciphertext = "wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}"

"""
Try all possible Caesar cipher shifts (1 to 25).
Print each result to find the correct decryption manually.
"""
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}")

