with open("output.txt") as f:
	content = f.read()

#defines p, ints from as in the file
exec(content)

for num in ints:
	if pow(num,(p-1)//2,p)==1:
		ans = pow(num,(p+1)//4,p)
		print(ans,p-ans)
