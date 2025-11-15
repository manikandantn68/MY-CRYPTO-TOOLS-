import base64

# Base64-encoded string
encoded = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg=="

# Decode and print
decoded = base64.b64decode(encoded).decode()
print("Decoded string:", decoded)

