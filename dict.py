dict = {'name':'ash','code':6734,'dept':'sales'}
print(dict)
print(dict.keys())
print(dict.values())
newlist = list()
for i in dict.keys():
    newlist.append(i)
print(newlist)

newvalues= list()
for i in dict.values():
    newvalues.append(i)
print(newvalues)

a = 12
print(chr(a))

a=10
b=20
print(a**b)
print(a//b)
print(a/b)

# read char in string
a_string = "Ashwini"
for letter in a_string:
    print(letter,end = " ")

#string revers

a_string = "Ashwini"
print("string before revese")
def reversstr(a_string):
    return a_string[::-1]

print(reversstr(a_string))

#String split

a = "ashwini r doke"
b=a.split()
print(b)

#Prime number
print("enter number")
num  = input()
num = int(num)
if num > 1:
    for i in range (2,num):
         if(num%i==0):
            print(num," is not prime number ")
            break
         
    print(num, " is prime number" )

