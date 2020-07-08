from pwn import xor

s1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
s2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
s3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
f = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


# Hex strings need to be converted to bytes prior to xor
x1 = bytes.fromhex(s1)
x2 = bytes.fromhex(s2)
x3 = bytes.fromhex(s3)
f = bytes.fromhex(f)


k1 = x1
k2 = xor(x2,x1)
k3 = xor(k2,x3)
flag = xor(k1,k2,k3,f)

print(flag)