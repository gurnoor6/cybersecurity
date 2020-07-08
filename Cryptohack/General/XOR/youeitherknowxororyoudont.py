from pwn import xor

s = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
key = "myXORkey"
x1 = bytes.fromhex(s)
x2 = key.encode()
print(xor(x1,x2))




#Did this process manually
# s = "04"
# x = bytes.fromhex(s)

# for i in range(256):
# 	b = bytes([i])
# 	ans = xor(b,x)
# 	print(b,ans)

# # Key
# m y X O R k e y