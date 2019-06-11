class node:
    def __init__(self) :
        self.data=None
        self.next=None
    def set_data(self,data) :
        self.data=data
    def set_next(self) :
        self.next=next
    def get_data() :
        return self.data
    def get_next() :
        return self.next
    def has_next() :
        return self.next != None

class linked_list:
    def __init__(self,head = None) :
        self.head = head
        self.size = 0
    def print_list(self):
        current=self.head
        while current:
            print(current.data)
            current=current.get_next()

    def insert_at_begining(self,data):
        new_node=node()
        new_node.set_data(data)
        if self.head ==None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head=new_node
            self.length += 1
    

mylist = linked_list()
print("********** inserting *************")
mylist.insert_at_begining(20)
#mylist.insert_at_begining(15)
mylist.print_list()     
