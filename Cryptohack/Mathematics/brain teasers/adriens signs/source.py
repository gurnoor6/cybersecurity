from random import randint
from Crypto.Util.number import inverse, long_to_bytes
import math

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext

def decrypt_flag(l,s):
    for num in l:
        if pow(num,(p-1)//2,p)==1:
            s+="1"
            continue
        s+="0"
    return s
    
with open("output.txt") as f:
    contents = f.read()
exec(contents)
s = decrypt_flag(l,"")
s = int(s,2)
print(long_to_bytes(s))