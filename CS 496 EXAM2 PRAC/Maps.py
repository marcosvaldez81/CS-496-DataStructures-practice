
#############################

# Maps Practice

#############################





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

if __name__ == '__main__':
    myMap = {'a':1, 'b':2, 'c':3}
    myMap2 = D(myMap)
    print("A is: ", myMap2.get('a'))
    print("Length is: ", myMap2.__len__())
    print("Iteration:  ", myMap2.__iter__())
    print()
    print("Setting A to 55:")
    myMap2.__setitem__('a', 55)
    print("New A is: ", myMap2.__getitem__('a'))
    print()
    print("Going to delete C now!")
    myMap2.__delitem__('c')
    print("New dictionary: ", myMap2.__len__())

