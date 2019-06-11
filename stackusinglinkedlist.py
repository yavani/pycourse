class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
    

class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None :
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head=new_Node
           # return new_node
    def pop(self):
        if self.head is None :
            return None
        else: 
            poped = selaf.head.data
            self.head = self.head.next
            return poped


stack = linkedlist()
newnode=stack.push("10")
print(newnode)

