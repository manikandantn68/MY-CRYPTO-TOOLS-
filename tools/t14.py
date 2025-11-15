import binascii

# RSA parameters
p = 2196739273872067284049398848323
q = 94285533320544671861528774696183
e = 65537
c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n = p * q
phi = (p - 1) * (q - 1)

# Compute private key d
d = pow(e, -1, phi)

# Decrypt ciphertext
m = pow(c, d, n)

# Convert to hex and decode
hex_m = hex(m)[2:]
if len(hex_m) % 2 != 0:
    hex_m = "0" + hex_m

try:
    decoded = binascii.unhexlify(hex_m).decode()
except Exception as err:
    decoded = f"[Decoding failed] {err}"

# Print results
print("Decrypted integer:", m)
print("Hex:", hex_m)
print("Decoded message:", decoded)

