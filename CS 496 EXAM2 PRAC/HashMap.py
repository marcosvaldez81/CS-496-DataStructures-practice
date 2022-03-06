#############################

# HashMap Base Practice

#############################


from _collections_abc import MutableMapping
import random

class MapBase(MutableMapping):
    
    class _Item:
        __slots__ = '_key', '_value'
        
        
        def __init__(self,key,value):
            self._key = key 
            self._value = value 
            
        def __eq__(self,other): # compare items see if equal 
            return self._key == other._key 
        
        def __ne__(self,other): # compare if they are not equal 
            return not (self == other) 
        
        def _iterator__(self,other): # compare iterator
            return self._key < other._key 

class HashMapBase(MapBase):
    
    """ Abstract base class for map using hash-table with MAD compression """
    
    def __init__(self, cap = 11, p = 109345121):
        """ Create an empty hash-table map """
        
        self._table = cap * [None]
        self._n = 0 # # of entries 
        self._prime = p  # prime for mad compression 
        self._scale = 1 + random.randrange(p-1) # scale from 1 to p-1 for MAD
        self._shift = random.randrange(p) # shift from 0 to p-1 for MAD
        
        
    def _hash_function(self,key):
        return (hash(key)* self._scale + self._shift) % self._prime % len(self._table)
    
    
    def __len__(self):
        return self._n
    
    
    def __getitem__(self, key):
        j = self._hash_function(key)
        return self._bucket_getitem(j,key) # may raise Key Err
        
    def __setitem__(self,key,value):
        j = self._hash_function(key)
        
        self._bucket_setitem(j,key,value)
        if self._n > len(self._table) //2:
            self._resize(2*len(self._table) - 1)
            
            
    def __delitem__(self,key):
        j = self._hash_function(key)
        self._bucket_delitem(j,key)
        self._n -=1
        
    def _resize(self,c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0 
        for (key,value) in old:
            self[key] = value 






class ChainHashMap(HashMapBase):
    """ hash map implemented with separate chaining for collision resolution """
    
    
    
    def _bucket_getitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))
        return bucket[k]
    
    
    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap() 
        oldsize = len(self._table[j])
        
        self._table[j][k] = v 
        if len(self._table[j]) > oldsize:
            self._n +=1 
            
    
    def _bucket_delitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ', repr(k))
        del bucket[k]
        
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key 
    
