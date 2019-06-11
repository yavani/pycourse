import random
def generateone(strlen):
           alphabet="abcdefghijklmnopqrstuvwxyz "
           res=""
           for i in range(strlen):
                   res = res + alphabet[random.randrange(27)]
           return res
  #print(generateone(28))
def score(goal,teststring):
          numsame=0
          for i in range(len(goal)):
                  if goal[i]== teststring[i]:
                          numsame=numsame+1
          return numsame/len(goal)
 
def main():
	print("ashwini") 
	goalstring="we think its easy"
	newstring=generateone(28)
	best=0
	print("aaaaaaaaaaaaaa")	
	newscore=score(goalstring,newstring)
	print(newscore)
	while newscore<1:
		if newscore>best:
			print(newscore,newstring)
			best=newscore
		newstring= generateone(28)
		newscore=score(goalstring,newstring)
 
main()
