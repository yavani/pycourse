def seqsearch(alist,item):
     pos=0
     found=False 
     while pos<len(alist) and not found:
        if alist[pos]==item:
               found=True
               print(f"Item {alist[pos]} is present and found")
        else:
                pos=pos+1
     return found   

print(f"Item  is not present in list")

alist=[1,2,4,3,6,89,9,76]
seqsearch(alist,5)

