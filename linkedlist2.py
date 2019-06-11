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
        while currentnode is not None:
            length += 1
            currentnode = currentnode.next
        return length
 
    def insert_at_head(self,newnode):
        temp = self.head
        self.head = newnode
        self.head.next = temp
        del temp

    def insert(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
              
                lastnode = lastnode.next
            lastnode.next = newnode

    def insertat(self,newnode,pos):
        #print("hello")
        if pos == 0:
           self.insert_at_head(newnode)
           return
        if pos < 0  or pos > self.listlength():
            print("invalid postion ! enter corrent pos")
            return
        currentnode = self.head
        currentpos = 0
        while True:
            if currentpos == pos:
                previousnode.next = newnode
                newnode.next = currentnode
                break   
            previousnode = currentnode
           # print("hey")
            currentnode = currentnode.next
            currentpos += 1   
    
    def printlist(self):
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next
              

firstnode = Node(10)
ll = linkedlist()
ll.insert(firstnode)
secondnode = Node(20)
ll.insert(secondnode)
thirdnode = Node(30)
ll.insert(thirdnode)
forthnode = Node(50)
ll.insert_at_head(forthnode)
fifth = Node(60)
ll.insert(fifth)
sixth = Node(70)
ll.insert_at_head(sixth)
#print("hi")
seventh= Node("Ashwini")
ll.insertat(seventh,2)
eight = Node("malhar")
ll.insertat(eight, -1)
ll.insertat(eight,5)
nine = Node("start")
ll.insertat(nine,0)
length=ll.listlength()

ll.printlist()

print(f"length of list is { length}")
