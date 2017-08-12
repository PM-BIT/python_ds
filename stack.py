class myStack:
     def __init__(self,limit):
         self.stack = []  # You don't want to assign [] to self - when you do that, you're just assigning to a new local variable called `self`.  You want your stack to *have* a list, not *be* a list.
         self.limit=limit
     def isEmpty(self):
         return self.size() == 0   # While there's nothing wrong with self.container == [], there is a builtin function for that purpose, so we may as well use it.  And while we're at it, it's often nice to use your own internal functions, so behavior is more consistent.

     def push(self, item):
         if (self.size()<self.limit):
             
             self.stack.append(item)  # appending to the *container*, not the instance itself.
         else:
             print("Stack Overflow!")
         

     def pop(self):

         if self.size()>0:
             
             return self.stack.pop()  # pop from the container, this was fixed from the old version which was wrong
         else:
             print("Stack Underflow!!!")

     def size(self):
         return len(self.stack)

     def check_balance(self):                            ####This function checks if the aprenthesis is balanced in an expression using Stack.Create a stack with myStack and use this function.
          
          topsymbol=None
          balanced=True
          stri=raw_input("Enter string to check\n")
          symbolstack=self
          for symbols in stri:
               if symbols in ["(","{","["]:
                    symbolstack.push(symbols)
               if symbols in [")","}","]"]:
                    topsymbol=symbolstack.pop()
                    if topsymbol is "(" and symbols is not ")":
                         balanced= False
                         exit
                    if topsymbol is "{" and symbols is not "}":
                         balanced=False
                         exit
                    if topsymbol is "[" and symbols is not "]":
                         balanced=False
                         exit
                    
          return balanced
               
                         


     
                         
               
          
          



                        #LINKED LIST IMPLEMENTATION FOR STACK

class Node:
        
        
        def __init__(self):
                self.data = None
                self.next = None

        def getData(self):
                return self.data

        def getNext(self):
                return self.next

        def setData(self,newdata):
                self.data = newdata
            
        

        def setNext(self,newnext):
                self.next = newnext



class Stack :
    

     def __init__(self):
        self.head=None
        

     def push(self,data):
        
        temp=Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head=temp
        
     def pop(self):
        
          if self.head is None:
               print("StackUnderflow!!")
          else:
             
               temp=self.head.getData()
               self.head=self.head.getNext()
        
               return temp
     def peek(self):                      #peek only shows the head elememt ,doesn't take it out,whereas pop takes it out
          
          if self.head is None:
               print("No data to peek")
          else:
               return self.head.getData()

     
               


     
                    
          
    
        
    


