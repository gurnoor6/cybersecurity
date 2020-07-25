import math
from decimal import *
getcontext().prec = 100

FLAG = "crypto{???????????????}"
FLAG = "crypto{"
print(len(FLAG))
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
PRIMES = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
print(len(PRIMES))
h = Decimal(0.0)
for i, c in enumerate(FLAG):
    h += ord(c) * Decimal(PRIMES[i]).sqrt()

# h+=ord('}')*Decimal(PRIMES[22]).sqrt()
# print(f"h= {h}")

# h = 3335.240163456235922599989478466430980002675256354192425543701971658455403187444370057160641956539904

ct = math.floor(h*16**64)
print(f"ciphertext: {ct}")

# ciphertext: 1350995397927355657956786955603012410260017344805998076702828160316695004588429433
