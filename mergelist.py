class Node:
    def __init__(self,data):
         self.data = data
         self.next = None

class linkedlist:
    def __init__(self):
       self.head = None

    def listlength(self):
       currentnode = self.head
       length = 0
       if currentnode is not None:
          length += 1
          currentnode = currentnode.next
       return length

    def insertathead(self , newnode):
        temp = self.head
        self.head = newnode
        newnode.next = temp

    def insert_at_end(self,newnode):
        if self.head is None:
           self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode

    def merglist(self,list1,list2,merglist):
        currentfirst = list1.head
        currentsecond =list2.head
        while True:
            if currentfirst is None:
                merglist.insert_at_end(currentsecond)
                break
            if currentsecond is None:
                mergelist.insert_at_end(currentfirst)
                break
            if currentfirst.data < currentsecond.data:
               currentfirstnext = currentfirst.next
               currentfirst.next = None
               mergelist.insert_at_end(currentfirst)
               currentfirst = currentfirst.next
            else:
                currentsecondnext = currentsecond.next
                currentsecond.next = None
                mergelist.insert_at_end(currentsecond)
                currentsecond = currentsecond.next

    def printlist(self):
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next

first = Node(10)
ll = linkedlist()
ll.insertathead(first)
#ll.printlist()
second = Node(20)
ll.insert_at_end(second)
#ll.printlist()
third = Node(30)
ll.insert_at_end(third)
ll.printlist()

l2 = linkedlist()
fourth = Node(15)
l2.insertathead(fourth)
fifth = Node(25)
l2.insert_at_end(fifth)
sixth = Node(40)
l2.insert_at_end(sixth)

l2.printlist()


mergelist = linkedlist()
mergelist.merglist(ll,l2,mergelist)
print("*********merged list*****")
mergelist.printlist()
