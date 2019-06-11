class fraction:
	def __init__(self,m,n):
		self.num=m
		self.den=n
	def __str__(self):
		return str(self.num)+"/"+str(self.den)
	def getnum(self):
		return self.num
	def getden(self):
		return self.den

num=input("enter numerator")
den=input("enter denominator")
f1= fraction(num,den)
print("numerator is :",num)
print("denominator is:",den)
print(f1)
f1.getnum()
f1.getden()


