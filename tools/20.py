nums = [104, 372, 110, 436, 262, 173, 354, 393, 351, 297, 241, 86, 262, 359, 256, 441, 124, 154, 165, 165, 219, 288, 42]
charset = {i: chr(96 + i) for i in range(1, 27)}  # a-z
charset.update({i: str(i - 27) for i in range(27, 37)})  # 0-9
charset[37] = "_"

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

decoded = ""
for n in nums:
    r = n % 41
    inv = modinv(r, 41)
    decoded += charset.get(inv, "?")

print("picoCTF{" + decoded + "}")

