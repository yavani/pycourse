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

    def merge_sorted(self,llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q :
           if p.data <= q.data:
              s = p
              p = s.next
           else:
               s = q
               q = s.next
           newhead = s
        while p and q:
            if p.data <= q.data :
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return newhead 
          
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
print("list1 is below ")
ll.printlist()

l2 = linkedlist()
fourth = Node(15)
l2.insertathead(fourth)
fifth = Node(25)
l2.insert_at_end(fifth)
sixth = Node(40)
l2.insert_at_end(sixth)
print("list 2 is below")
l2.printlist()

l2.merge_sorted(ll)
print("************merged list ***************")
ll.printlist()


