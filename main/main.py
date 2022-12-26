from funcs import encode, decode
import os

for f in os.listdir("output"): #include path
    enc = encode("output\\"+f)

    dec = decode(enc)