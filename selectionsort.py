def selectionsort(list):
    for i in range (len(list)-1):
         minvalue=i
         for j in range(i,len(list)):
             if list[j]<list[minvalue]:
                 minvalue=j
         temp=list[i]
         list[i]=list[minvalue]
         list[minvalue]=temp
         print(list)
list=[5,3,8,6,7,2]
#list=int(list)
selectionsort(list)
print(list)
