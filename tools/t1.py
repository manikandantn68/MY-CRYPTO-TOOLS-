from Crypto.Util.number import getPrime, bytes_to_long, inverse
from sys import exit

# Public exponent (standard RSA value)
e = 65537

# This function will give two prime numbers (p, q)
def get_primes(bits):
    p = getPrime(bits)
    q = getPrime(bits)
    return p, q

def make_keys(bits):
    p, q = get_primes(bits // 2)
    N = p * q
    d = inverse(e, (p - 1) * (q - 1))
    return (N, e), d

def encrypt_message(public_key, message):
    N, e = public_key
    m_num = bytes_to_long(message.encode('utf-8'))
    cipher = pow(m_num, e, N)
    return cipher

def main(flag_text):
    public_key, _ = make_keys(1024)
    cipher = encrypt_message(public_key, flag_text)
    return public_key[0], cipher

if __name__ == "__main__":
    # You can create a flag.txt or just hardcode the message below
    try:
        with open('flag.txt', 'r') as f:
            flag = f.read().strip()
    except FileNotFoundError:
        flag = "Hello_RSA_Test"

    N, cipher = main(flag)

    print("N:", N)
    print("e:", e)
    print("Encrypted message:", cipher)
    exit()
