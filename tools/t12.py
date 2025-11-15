#!/usr/bin/python
from pwn import *

enc_flag = bytes.fromhex("551257106e1a52095f654f510a6b4954026c1e0304394100043a1c5654505b6b")  # complete hex string
enc_text = bytes.fromhex("236625611d392070281d3971731d3922251d3923201d3922751d392423702f1d")  # complete hex string
dec_text = b'A' * len(enc_text)

key = xor(enc_text, dec_text)
print(xor(enc_flag, key).decode())

