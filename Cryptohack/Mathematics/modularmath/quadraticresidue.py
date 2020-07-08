l = [14,6,11]
p = 29

for i in range(29):
	x = (i**2)%p
	if x in l:
		print(i,29-i)
		break
