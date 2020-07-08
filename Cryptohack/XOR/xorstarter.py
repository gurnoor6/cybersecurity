s = "label"
x = 13
l = [ord(x) for x in s]
for i in range(len(l)):
	l[i] = chr(l[i]^x)

print(l)