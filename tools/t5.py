import codecs

# ROT13 encoded string
encoded = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"

# Decode using ROT13
decoded = codecs.decode(encoded, 'rot_13')

print("Decoded:", decoded)

