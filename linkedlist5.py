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

    def findnth (self,n):
        print("hi")
        p = self.head
        f = self.head
        cnt = 1
        while cnt <= n-1:
            f = f.next
            cnt += 1
        while f.next is not None:
            f = f.next
            p = p.next
        print(p.data)

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

fourth = Node(15)
ll.insertathead(fourth)
fifth = Node(25)
ll.insert_at_end(fifth)
sixth = Node(40)
ll.insert_at_end(sixth)
print("list  is below")
ll.printlist()
n = input("enter the position number  ")
n = int(n)
ll.findnth(n)

