import linkedlist5

def findnth(self,n):
    p =self.head
    f = self.head
    cnt = 1
    while cnt <= n-1:
        f = f.next
        cnt +=1
    while f.next is not None:
        f = f.next
        p = p.next
    print(p.data)


ll = linkedlist()
first = Node(10)
ll.insert_at_end(first)
print(ll)
