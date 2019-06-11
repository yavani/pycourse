def binarysearch(alist,item):
     first=0
     last=len(alist)-1
     found = False
     while first<=last and not found:
           midpoint= first+last//2
           if alist[midpoint]==item:
              found= true
           else:
                if item < alist[midpoint]:
           	      last= midpoint-1
                else:
                      first=midpoint+1
     return found

alist=[2,3,40,10,60,45,90,80]
print(binarysearch(alist,45))

