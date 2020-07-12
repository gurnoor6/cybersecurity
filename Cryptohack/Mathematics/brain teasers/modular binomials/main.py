import math

with open("data.txt") as f:
	content = f.read()
exec(content)

e1e2 = e1*e2
qe1e2 = (pow(5,e1e2,N)*pow(c1,e2,N)-pow(2,e1e2,N)*pow(c2,e1,N))%N
pe1e2 = (pow(3,e1e2,N)*pow(c2,e1,N)-pow(7,e1e2,N)*pow(c1,e2,N))%N

p  = math.gcd(N,pe1e2)
q = math.gcd(N,qe1e2)
#  Not exactly the answer
print("crypto{},{}".format(p,q))
