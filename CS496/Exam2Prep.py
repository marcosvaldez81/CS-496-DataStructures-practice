################################################################################



# Marcos Valdez 
# CS 496
# This script will hold all major class functions for data structures final

################################################################################


# PRIORITY QUEUES: 


# Base Priority Queue Class
class PriorityQueueBase:
    """ Base class for a priority queue """
    class _Item:
        """ To store priority queue items """
       
        __slots__ = '_key', '_value'
       
        def __init__(self,k,v):
            self._key = k
            self._value = v
           
        def __item__(self,other):
            return self._key < other._key # Compares the items based on their keys
           
        def is_empty(self): # returns true if priority queue is empty.
            return len(self) ==0


# ------------------------------------------------------------------

# Remove the highest number of a queue: 

class PriorityQueue(object):
   
    def __init__(self):
        self.queue = []
       
   
    # convert to a string
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
       
       
    # this function is to to convert to string
   
    def isEmpty(self):
        return len(self.queue)==0
       
    # insert function for priority queue
    def insert(self, item):
        self.queue.append(item)
       
    # to delete from highest number to lower. Can flip the for loop if conditional to "<" if wanting to do less than
    def delete(self):
        try:
            max = 0
           
            for i in range(len(self.queue)):
                if (self.queue[i] > self.queue[max]):
                    max = i
            item2 = self.queue[max]
               
            del self.queue[max]
            return item2
           
        except:
            print("Err")
            exit()
       
   
#    
# if __name__ == '__main__':
#     queue = PriorityQueue()
#     queue.insert(15)
#     queue.insert(5)
#     queue.insert(2)
#     queue.insert(100)
#    
#     print(queue)
#    
#     while not(queue.isEmpty()):
#         print(queue.delete())







# ---------------------------------------------

# RUN TIME HEAP:
    # Unsorted list : O(1) insertion, O(n) access
    # sorted : O(1) access, O(n) insertion
    
    
    
# PYTHON HEAP IMPLEMENTATION:

class HeapPriorityQueue(PriorityQueueBase): # base class defines _Item look up^^
    
    """ Min-Oriented priority queue implemented w/ a binary heap """
    
    
    def _parent(self,j):
        return (j-1)//2
    
    def _left(self,j):
        return 2*j + 1
    
    def _right(self,j):
        return 2*j + 2
    
    def _has_left(self,j):
        return self._left(j) < len(self._data) #index beyond end of list?
    
    def _has_right(self,j):
        return self._right(j) < len(self._data)
    
    
    def _swap(self,i,j):
        """ swap elements at indices i and j of array """
        
        self._data[i],self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)
    
    def _downheap(self,j):
        
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            
            if self._data[small_child] < self._data[j]:
                self._swap(j,small_child)
                self._downheap(small_child)
    
    
    
    
    def __init__(self):
        """ Create empty priority queue """
        
        self._data = [] 
        
    def __len__(self):
        "return # of items in queue"
        
        return len(self._data)
    
    
    def add(self,key,value):
        """ Add key value pair to priority queue """
        
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data) - 1)


    def min(self):
        # if empty:
        
        if self.isEmpty():
            raise Empty("Priority queue is empty")
        
        item = self._data[0]
        return (item._key, item._value)
    def remove_min(self):
        if self.isEmpty():
            raise Empty("Priority queue is empty")
        self._swap(0,len(self._data) - 1)
        item = self._data.pop() 
        self._downheap(0)
        return (item._key, item._value)


        
# ------------------------------------------------------------------


# MAPS 

# main ops of a map is: searching inserting and deleting
# multiple items with same key are NOT allowed
# unsorted map = LIST
# Applications: address Book and student-record base
# run time of LIST BASED MAP: Inserting an item takes O(1) for unsorted list , searching/removing takes O(n) time

# THIS CLASS D IS THE ABSTRACT METHOD WE NEED BEFORE CUSTOM CLASS

from collections.abc import MutableMapping

# Dictionary mutable mapping: 
class D(MutableMapping):
    
    
    def __init__(self,*k,**v):
        self.__dict__.update(*k,**v)
        
        
    def __getitem__(self, key):
        return self.__dict__[key]
    
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value  
        

    def __len__(self):
        return len(self.__dict__)  
    

    def __delitem__(self, key):
        del self.__dict__[key]

    
    def __iter__(self):
        return iter(self.__dict__)
    

# LIST MUTABLE MAPPING:


# class ListBasedSet(MutableMapping):
#     def __init__(self, iterable):
#         
#         self.













# custom abstract class:

class MapBase(MutableMapping):
    
    """ Our own abstract base class that includes a nonPublic _Item class. """
    
    
    class _Item: 
        """ To store key-value pairs """
        
        __slots__ = '_key', '_value'
        
        def __init__(self, k,v):
            self._key = k 
            self._value = v
            
        def __equal__(self, other):
            return self._key == other._key # if keys equal
        
        def __not_equeal__(self, other): # if not equal
            return not (self == other)
        
        def __lt__(self,other): # larger than?
            return self._key < other._key
        


# THIS IF BLOCK IS FOR DICTIONARY MUTABLE MAPPING 

# if __name__ == '__main__':
#     myMap = {'a':1, 'b':2, 'c':3}
#     myMap2 = D(myMap)
#     print("A is: ", myMap2.get('a'))
#     print("Length is: ", myMap2.__len__())
#     print("Iteration:  ", myMap2.__iter__())
#     print()
#     print("Setting A to 55:")
#     myMap2.__setitem__('a', 55)
#     print("New A is: ", myMap2.__getitem__('a'))
#     print()
#     print("Going to delete C now!")
#     myMap2.__delitem__('c')
#     print("New dictionary: ", myMap2.__len__())


# ----------------------------------------------


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

# test = Node(50) #top of tree
# test = insert(test,30)
# test = insert(test,20)
# test = insert(test,40)
# test = insert(test,70)
# test = insert(test,60)
# test = insert(test,80)
# 
# print("Inorder traversal of the given tree: ")
# inorder(test)
# 
# print()
# 
# print("Now going to delete 20 from tree")
# test = deleteNode(test,20)
# print(".")
# print(".")
# print(".")
# print("Done!")
# print("Let's see how the now modified tree looks: ")
# inorder(test)



#print(searchTree(test,30))


    