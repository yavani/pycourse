import Stack as mystack

def revstring(mystring):
      #mystack=Stack()
      for ch in mystring:
         mystack.push(ch)
      revstr= " "
      while not mystack.isEmpty():	     
         revstr= revstr+mystack.pop()
           
      return revstr


revstring("apple")
