enc = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"  # This is the encrypted input string (ROT13 encoded). You can assign any ROT13 string here.
text_clair = ""  # This will store the final decoded (plain text) result.

# Loop through each character in the encrypted string
for char in enc:
    ascii_char = ord(char)  # Convert the character to its ASCII numeric value

    # Check if the character is a lowercase letter (a-z)
    if 97 <= ascii_char <= 122:
        # Apply ROT13 transformation for lowercase letters
        ascii_char = (ascii_char - 97 + 13) % 26 + 97

    # Check if the character is an uppercase letter (A-Z)
    elif 65 <= ascii_char <= 90:
        # Apply ROT13 transformation for uppercase letters
        ascii_char = (ascii_char - 65 + 13) % 26 + 65

    # Convert the transformed ASCII value back to a character
    new_char = chr(ascii_char)

    # Append the decoded character to the result string
    text_clair += new_char

# Print the final decoded message
print(text_clair)

