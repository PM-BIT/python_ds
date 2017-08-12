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

        

class LinkedList:
        

        def __init__(self):
                self.head = None

        def add_at_beg(self,item):
                temp = Node(item)
                temp.setNext(self.head)
                self.head = temp
                
        def add_at_last(self,item):
                newNode=Node(item)
                #newNode.setData(item)
                current=self.head
                while current.getNext()!=None:
                        current=current.getNext()
                current.setNext(newNode)

        def add_at_pos(self,posi,data):
                pos=0
                if posi==1:
                        self.add_at_beg(data)
                elif posi==self.size():
                        self.add_at_last()
                else:
                        current=self.head
                        while current!=None:
                                pos=pos+1
                                if pos==posi-1:
                                        temp=Node(data)
                                        temp.setNext(current.getNext())
                                        current.setNext(temp)
                                        break
                                current=current.getNext()
                                        
                                
                
        def size(self):
                current = self.head
                count = 0
                while current != None:
                        count = count + 1
                        current = current.getNext()

                return count
        def print_list(self):
                current=self.head
                if self.size()>0:
                        
                        while current!=None:
                                print (current.getData())
                                current=current.getNext()
                else:
                        print("List is empty .Nothing to print")

        def search_in_list(self,item):
                current=self.head
                search_value=item
                pos_list=[]
                found=0
                count=0
                position=0
                while current!=None:
                        
                        data=current.getData()
                        position=position+1
                        
                        if data==search_value:
                                #print "Data found at index ",position
                                found=found+1
                                
                                pos_list.append(str(position))
                                current=current.getNext()
                                continue
                                
                                
                               
                        elif data!=search_value:
                                current=current.getNext()
                                continue
                
                                
                print "Data",item,"found at following indexes:"
                for item in pos_list:
                        print item
                                
                
                exit

        def delte_from_list(self,item):
                current=self.head
                position=0
                if self.size()>1:
                        while(current.getNext()!=None):
                                headdata=self.head.getData()
                        
                                data=current.getNext().getData()
                                position=position+1
                                if headdata==item:
                                        self.head=current.getNext()
                                if data==item :
                                        current.setNext(current.getNext().getNext())
                                
                                        break
                                elif data!=item:
                                        current=current.getNext()
                                        continue
                        
                                
                elif self.size()==0:
                        print"Nothing to delete"
                elif self.size()==1:
                        self.head=None
                        
                       
                
                                
        
             
             
        
        
    
