from Crypto.Util.number import long_to_bytes, bytes_to_long

def legendre(a, p):
    return pow(a, (p - 1) // 2, p)
 
def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def getAllPossibilites(ct,n,power):
	if legendre(ct,n)!=1 or power<1:
		return
	if b"crypto" in long_to_bytes(ct):
		print(long_to_bytes(ct))
		return
	getAllPossibilites(tonelli(ct,n),n,power//2)
	getAllPossibilites(n-tonelli(ct,n),n,power//2)
	

with open("data.txt") as f:
	contents = f.read()
exec(contents)

# l=[]
# x = tonelli(ct,n)
# l.append(x)
# l.append(n-x)

# x = tonelli(l[0],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[1],n)
# l.append(x)
# l.append(n-x)
# l = l[2:]

# x = tonelli(l[0],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[1],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[2],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[3],n)
# l.append(x)
# l.append(n-x)
# l = l[4:]

# l = l[:4]
# x = tonelli(l[0],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[1],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[2],n)
# l.append(x)
# l.append(n-x)
# x = tonelli(l[3],n)
# l.append(x)
# l.append(n-x)
# l = l[4:]

# print(long_to_bytes(l[0]))
# print(long_to_bytes(l[1]))
# print(long_to_bytes(l[2]))
# print(long_to_bytes(l[3]))


getAllPossibilites(ct,n,16)

# print(l)
# for x in l:
# 	print(long_to_bytes(x))