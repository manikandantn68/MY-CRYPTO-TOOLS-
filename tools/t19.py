nums = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
flag = ''.join([chars[n % 37] for n in nums])
print("picoCTF{" + flag + "}")

