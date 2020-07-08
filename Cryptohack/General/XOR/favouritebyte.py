from pwn import xor

s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
x = bytes.fromhex(s)

for i in range(256):
	b = bytes([i])
	try:
		ans = xor(x,b).decode()
		if "crypto" in ans:
			print(b)
			print(ans)
	except:
		continue