class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print (root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print (root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    


def minval(root):                       #minimum value in a binary tree without recursion
    current=root
    while current.l_child!=None:
        current=current.l_child
    return current.data

def maxval(root):                      #maximum value without recursion
    current=root
    while current.r_child!=None:
        current=current.r_child
    return current.data



def search_with_recursion(root,data_to_find):   #This function uses recursion to find if an element is in the binary tree, if yes it will return 1 else 0.
    current=root
    if not root:
        return 0
    if current.data==data_to_find:
        return 1
    else:
        temp=search_with_recursion(current.l_child,data_to_find)
        if temp==1:
            return temp
        else:
            return search_with_recursion(current.r_child,data_to_find)
   
    
def height(root):
    current=root
    l_count=0
    r_count=0
    if not root:
        return 0
    else:
        if current.l_child!=None:
            while(current.l_child!=None):
                current=current.l_child
                l_count=l_count+1
        else:
            l_count=0

        if current.r_child!=None:
            while(current.r_child!=None):
                current=current.r_child
                r_count=r_count+1
        else:
            r_count=0
    if l_count>r_count:
        print(l_count)
    else:
        print(r_count)
        
            
    
