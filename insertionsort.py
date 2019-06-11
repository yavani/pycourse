def insertionsort(list):
    for i in range(1,len(list)):
        curvalue=list[i]
        position=i
        while position>0 and list[position-1]>curvalue:
               list[position]=list[position-1]
               position=position-1
        list[position]=curvalue

    print(list)
   
list=[54,26,93,17,77,31,44,55,20]
insertionsort(list)
print(list)
