from Crypto.Util.number import *
from hashlib import sha256

with open("key.txt") as fh:
	contents = fh.read()
exec(contents)
flag = b"crypto{Immut4ble_m3ssag1ng}"
H = sha256(flag)
s = pow(bytes_to_long(H.digest()),d,N)
print(hex(s)[2:])