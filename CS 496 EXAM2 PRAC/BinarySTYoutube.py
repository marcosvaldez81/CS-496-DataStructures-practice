#############################
 
# Binary Search Tree Youtube Practice
 
#############################
 
# Binary search tree is a recursive Data Structure
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
         
         
    def add_child(self,data):
        if data == self.data: # checking to see if the item is already in the binary tree
            return 
         
        if data < self.data:
            # add data value in left subtree
             
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
                 
              
        else:
            # add value to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
         
 
    def in_order_traversal(self):
        elements = [] 
         
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
             
         
        # visit base node 
        elements.append(self.data)
         
         
        # visit right tree 
        if self.right:
            elements+= self.right.in_order_traversal()
         
        return elements 
     
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_max(self): # far right max leaf node
        if self.right is None:
            return self.data # this if block basically returns the leaf node value if the right is None
        
        return self.right.find_max() # keep recursively calling to go to far right
        
    def find_min(self): 
        if self.left is None: #this if block basically returns the leaf node value if the left is None
            return self.data 
        return self.left.find_min() # keep recursively calling to go farthest left node
    
    
    
    
    def delete(self,value):
        
        if value < self.data: # if value is less than current node (self.data)
            if self.left: # if left subtree, delete that value, if not it will automatically return null
                self.left = self.left.delete(value) # recursivley call function to delete value
                
        elif value > self.data: 
            if self.right:
                self.right = self.right.delete(value)
                
        else:
            if self.left is None and self.right is None: # reached last data point
                return None 
               
            if self.left is None:
                return self.right 
            
            if self.right is None:
                return self.right 
            
            minimum = self.right.find_min()
            self.data = minimum
            self.right = self.right.delete(minimum)
        
        return self 
            
        
         
 
def build_tree(elements):
    print("Building tree with these elements: ", elements)
    root = BinarySearchTreeNode(elements[0])
     
     
    for i in range(1,len(elements)):
        root.add_child(elements[i])
         
         
    return root 
 
if __name__ == '__main__':
#     countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
#     country_tree = build_tree(countries)
#  
#     print("UK is in the list? ", country_tree.search("UK"))
#     print("Sweden is in the list? ", country_tree.search("Sweden"))
    
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Is 20 in the list?", numbers_tree.search(20))
    print("Is 5 in the list?", numbers_tree.search(5))
    
    print() 
    print("Going to delete now!")
    numbers_tree.delete(20)
    print("After deleting 20: ", numbers_tree.in_order_traversal())
    
