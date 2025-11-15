from Crypto.Util.number import long_to_bytes, inverse
print("""
| Step | Operation               | Concept                 |
| ---- | ----------------------- | ----------------------- |
| 1    | Given `N, e, C`         | Public key + ciphertext |
| 2    | Find `q`                | Factorization           |
| 3    | Compute `φ(N)`          | RSA math                |
| 4    | Find `d`                | Modular inverse         |
| 5    | Compute `M = C^d mod N` | Decrypt                 |
| 6    | Convert to text         | Get final flag          |
""")




N = 20265146323135593697800418779615617643712138008293072312540262540850164415798961387519643240955563574367038688732265131679906664286307186071540778731371838
e = 65537
ciphertext = 14509671392616733116263368042613153397522838041535993358667650752615409367787827435034944492972804316844856059350250833394359492745026367729141744028265037
p = 10132573161567796848900209389807808821856069004146536156270131270425082207899480693759821620477781787183519344366132565839953332143153593035770389365685919
q = N // p  # Corrected

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(ciphertext, d, N)
flag = long_to_bytes(m).decode()

print("Decrypted flag:", flag)

"""
RSA public key parameters
N = 20265146323135593697800418779615617643712138008293072312540262540850164415798961387519643240955563574367038688732265131679906664286307186071540778731371838
e = 65537

Ciphertext (encrypted message)
ciphertext = 14509671392616733116263368042613153397522838041535993358667650752615409367787827435034944492972804316844856059350250833394359492745026367729141744028265037


One of the primes (p)
p = 10132573161567796848900209389807808821856069004146536156270131270425082207899480693759821620477781787183519344366132565839953332143153593035770389365685919

. Finding the other prime q
q = N // p

// → integer division.
Since  n = p * q -> q = N / p gives the other prime.
Compute φ(N) (Euler’s Totient) -> phi = (p - 1) * (q - 1)
φ(N) used for finding private key (d).
Mathematically, it counts how many numbers < N are coprime to N.


7. Find private key d
d = inverse(e, phi)
d×e≡1 (mod ϕ)
condition satify pandra main step

Decrypt the message
m = pow(ciphertext, d, N)
M=CdmodN -> formula
pow() in Python efficiently does modular exponentiation — fast even for 1000+ bit numbers.



| Step | Operation               | Concept                 |
| ---- | ----------------------- | ----------------------- |
| 1    | Given `N, e, C`         | Public key + ciphertext |
| 2    | Find `q`                | Factorization           |
| 3    | Compute `φ(N)`          | RSA math                |
| 4    | Find `d`                | Modular inverse         |
| 5    | Compute `M = C^d mod N` | Decrypt                 |
| 6    | Convert to text         | Get final flag          |



"""