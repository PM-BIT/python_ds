class Node:
        
        
        def __init__(self,initdata):
                self.data = initdata
                self.next = None

        def getData(self):
                return self.data

        def getNext(self):
                return self.next

        def setData(self,newdata):
                self.data = newdata
            
        

        def setNext(self,newnext):
                self.next = newnext

        

class CircularLinkedList:
        

        def __init__(self):
                self.head = None

        def add_at_last(self,item):
                temp = Node(item)
                if self.head==None:
                        self.head=temp
                        temp.setNext(self.head)
                        
                else:
                        current=self.head
                        while current.getNext()!=self.head:
                                current=current.getNext()
                        temp.setNext(self.head)
                        current.setNext(temp)
                        self.head=temp


        def add_at_start(self,item):
                temp=Node(item)
                
                temp.setNext(temp)
                current=self.head
                if self.head==None:
                        
                        temp.setNext(self.head)
                        self.head=temp
                else:
                        while current.getNext()!=self.head:
                                current=current.getNext()
                        temp.setNext(self.head)
                        
                        current.setNext(temp)
                        self.head=temp

                        
        def insert_at(self,pos,data):
                count=0
                if self.size()==0 or pos==1:
                        add_at_start(item)
                if pos==self.size()+1:
                        add_at_last(item)
                else:
                        current=self.head
                        while current.getNext()!=self.head:
                                count=count+1
                                if count==pos:
                                        temp=Node(item)
                                        temp.setNext(current.getNext())
                                        break
                                current=current.getNext()
                
        
                        
        def size(self):
                
                current=self.head
                count=1
                if self.head==None:
                        
                        count=0
                else:
                       
                        while current.getNext()!=self.head:
                                
                                count=count+1
                                current=current.getNext()    
                        
                return count

        def print_list(self):
                current=self.head
                if self.size()==0:
                        print "Nothing in list to print"
                else:
                        while current.getNext()!=self.head:
                                print (current.getData())
                                current=current.getNext()
                                continue
                        
                
                        
                        
                
                
                
                        

                
