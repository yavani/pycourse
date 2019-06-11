def bubblesort(alist):
    for passnum in range(len(alist)-1,0,-1):
         for i in range(passnum):
             if alist[i]> alist[i+1]:
                 temp=alist[i]
                 alist[i]=alist[i+1]
                 alist[i+1]=temp

alist=[3,1,5,3,4,2]
bubblesort(alist)
print(alist)
