#############################

# Heap Priority Queues Practice

#############################


# PYTHON HEAP IMPLEMENTATION:

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
    
    
    # ADD/INSERT
    def add(self,key,value):
        """ Add key value pair to priority queue """
        
        self._data.append(self._Item(key,value))
        self._upheap(len(self._data) - 1)


    def min(self):
        # if empty:
        
        if self.isEmpty():
            return self.is_empty()
        
        item = self._data[0]
        return (item._key, item._value)
    def remove_min(self):
        if self.isEmpty():
            return self.is_empty()
        self._swap(0,len(self._data) - 1)
        item = self._data.pop() 
        self._downheap(0)
        return (item._key, item._value)

