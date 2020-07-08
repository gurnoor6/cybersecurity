import numpy as np
v1 = np.array([4,1,3,-1])
v2 = np.array([2,1,-3,4])
v3 = np.array([1,0,-2,7])
v4 = np.array([6, 2, 9, -5])

l = [v1,v2,v3,v4]

for i in range(1,4):
	for j in range(i):
		x = np.dot(l[i],l[j])/(np.linalg.norm(l[j])**2)
		print("x=",x)
		l[i] = l[i] - np.multiply(x,l[j])

print(l)
print(np.dot(l[0],l[1]))

