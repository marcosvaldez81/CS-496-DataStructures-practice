

#############################

# BInary Search Tree Practice

#############################

# This class is to create a node, overall the code below is to demonstrate insert operation for binary search tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



# insert function to  insert a new node with given Key

def insert(root, key):
   
    if root is None:
        return Node(key)
       
    else:
        if root.val == key:
            return root
           
        elif root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
           
    return root
 
# this is a inorder tree traversal function  
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
       
       
def searchTree(root, key):
    """ Binary search tree """
   
    if root is None or root.val == key: # if root is null or key is present at root
   
        return root # return root
       
    if root.val < key: # key is greater than root's key
        return searchTree(root.right,key)
       
    return searchTree(root.left,key) #if key is smaller than root's key
   
   

# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched
def minValueNode(Node):
    current = Node
   
    # loop to find leftmost leaf
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(root, key):
   
    # Base Case
    if root is None:
        return root
       
   
    # If the key to be deleted is smaller than the root's key then it lies in  left subtree
   
    if key < root.val:
        root.left = deleteNode(root.left,key)
     
    # If the key to be deleted is greater than the root's key then it lies in  right subtree
    elif(key > root.val):
        root.right = deleteNode(root.right,key)
   
    # Else key is same as root's key, then this is the node to be deleted
    else:
       
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
           
       
        # node w/ 2 children, get the inorder successor (smallest in right subtree)
        temp = minValueNode(root.right)
       
        # copy the inorder successor content to this node
       
        root.key = temp.val
       
        #delete the inorder successor
        root.right = deleteNode(root.right,temp.val)
   
   
    return root
   
   
#Driver program to test the above functions
# Let us create the following Binary ST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

test = Node(50) #top of tree
test = insert(test,30)
test = insert(test,20)
test = insert(test,40)
test = insert(test,70)
test = insert(test,60)
test = insert(test,80)
 
print("Inorder traversal of the given tree: ")
inorder(test)
 
print()
 
print("Now going to delete 20 from tree")
test = deleteNode(test,20)
print(".")
print(".")
print(".")
print("Done!")
print("Let's see how the now modified tree looks: ")
inorder(test)
 
 
  
print(searchTree(test,30))
