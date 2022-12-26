from funcs import encode, decode
import os

for f in os.listdir("input"): #include path
    enc = encode("input\\"+f)

    dec = decode(enc)