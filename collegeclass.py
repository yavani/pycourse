class college:
	def __init__(self,name,city):
	     self.name=name
	     self.city=city
	     print(f" NAMHA SHIVAY !! Welcome to {name} school of engineering {city}")
	     #print("my college location is",city)
	    	
	def login(self):
	     print("please enter login credintials")
	     username=input("enter your user name")
	     password=input("please enter password")
	     print(f"welcome !! {username} ")
	
class department(college):
	def select(self):
		print("enter the department of your choice ")
		dept = input(">>")
		if dept =="cse":
	    		  print(""" you are at computer science department
		                 it offres below courses 
		     		 1. Btech
		      		 2. Mtech
		     		 3. PHD """)
	    
class staff(college):
	def facultyinfo(self,name):
	      self.name=name
	      print("enter your department name ")
	      dept= input(">>")
	      print(f" I am {name} from {dept} department ")

a= input("enter collge name  ")
b=input("enter college city  ")
st=department(a,b)
st.login()
st.select()
c= input("enter your name  ")
dt=staff(a,b)
dt.facultyinfo(c)



	    
