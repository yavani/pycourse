def gcd(m,n):
	while m % n !=0:
	      oldm=n
	      oldn=n

	      m=oldn
	      n=oldm%oldn
	      m=int(m)
	      n=int(n)
	return n

class fraction:
	def __init__(self,m,n):
	   self.num=m
	   self.den=n
	   print("***")
	   common= gcd(m,n)
	   print(common)
	   newnum= m//common
	   newden= n//common
	def __str__(self):
	   return str(self.newnum)+"/"+str(self.newden)

f1= fraction(6,8)
print(f1)


