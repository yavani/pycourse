class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:
   def __init__(self):
      self.head= None
   def insert(self,newnode):
      if self.head is None:
          self.head = newnode
      else:
          lastnode = self.head
          while True:
               if lastnode.next is None:
                   break
               lastnode = lastnode.next
          lastnode.next=newnode
   def printlist(self):
        currentnode= self.head
        print(currentnode)
        while True:
            if currentnode is None:
                break
        print(currentnode.data)
        currentnode = currentnode.next
             
'''create first node of linkedlist
   node -> data,next
'''
firstnode = node("sonal")
''' add it to linked list
   firstnode.data=10, firstnode.next=none
'''
linkedlist = linkedlist()
secondnode = node("malhar")
linkedlist.insert(firstnode)
linkedlist.insert(secondnode)
print("hiiiiii")
linkedlist.printlist()
print("hello")



