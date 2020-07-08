def gcd(x,y):
	if x%y==0:
		return y
	return gcd(y,x%y)

print(gcd(66528,52920))

