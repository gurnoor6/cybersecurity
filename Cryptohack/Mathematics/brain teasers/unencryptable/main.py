# from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
# import math

# # c = int("5233da71cc1dc1c5f21039f51eb51c80657e1af217d563aa25a8104a4e84a42379040ecdfdd5afa191156ccb40b6f188f4ad96c58922428c4c0bc17fd5384456853e139afde40c3f95988879629297f48d0efa6b335716a4c24bfee36f714d34a4e810a9689e93a0af8502528844ae578100b0188a2790518c695c095c9d677b",16)
N = 89820998365358013473897522178239129504456795742012047145284663770709932773990122507570315308220128739656230032209252739482850153821841585443253284474483254217510876146854423759901130591536438014306597399390867386257374956301247066160070998068007088716177575177441106230294270738703222381930945708365089958721
# def decrypt(c,e,N=N):
# 	for i in range(9,2048):
# 		print(f"i={i}")
# 		# if c!=pow(c,pow(2,i)+1,N):
# 		# 	print("here",c)
# 		# 	return
# 		if b"crypto" in long_to_bytes(pow(c,pow(2,i)+1,N)):
# 			print(long_to_bytes(pow(c,pow(2,i)+1,N)))
# 			return
# 		print(long_to_bytes(pow(c,pow(2,i)+1,N)))

# c = int("372f0e88f6f7189da7c06ed49e87e0664b988ecbee583586dfd1c6af99bf20345ae7442012c6807b3493d8936f5b48e553f614754deb3da6230fa1e16a8d5953a94c886699fc2bf409556264d5dced76a1780a90fd22f3701fdbcb183ddab4046affdc4dc6379090f79f4cd50673b24d0b08458cdbe509d60a4ad88a7b4e2921",16)
# decrypt(c,65537)

# print(pow(c,(N-1)//2,N))
# print(math.gcd(c,N))
# print(c)
# for j in range(2,77):
# 	for i in range(77):
# 		if pow(j,i,77)==j:
# 			print(j,i-1)
# 	print("\n")

# for i in range(1000):
# 	if(N%(pow(2,i)+1))
import math

c = 38751393103897326984966225657881797063081924259265913066269771931771353744954287558965505880351932624445905856402225526480435627356053320503495920770512272409426395361140215523926174575229867615188057195850608691252103369249627456812445758919344593590045677681290101112949924842617295206821539602559851702561
# for i in range(-100000,100000):
# 	if math.gcd(c+i,N)!=1:
# 		print(i)
i=2
while i<100000000:
	if c%i==0:
		print(i)
		c//=i
	i+=1