 #############################

# Hash Table Youtube Practice

#############################


# hash table class
class HashTable:
    
    def __init__(self):
        self.MAX = 10
        
        self.arr = [[] for i in range(self.MAX)]
        
        
    def get_hash (self,key):
        hash = 0 
        for char in key:
            hash += ord(char)
        return hash % self.MAX 
    
    def __getitem__(self,index):
        h = self.get_hash(index)
        for element in self.arr[h]:
            if element[0] == index:
                return element[1]
        
        
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False 
        # this for loop is to handle chainhash table! Error handling the hash map
        for index, element in enumerate(self.arr[h]): # enumerate is a function to iterate through elements of array
            if len(element) ==2 and element[0] == key:
                self.arr[h][index]= (key,val)
                found = True     
          
        if not found:
            self.arr[h].append((key,val))       


    def __delitem__(self,key):
        
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                

# Test Driver Code:

t = HashTable() 

t.__setitem__("Marcos", 0)
t.__setitem__("Ysenia", 1)
t.__setitem__("Jeremiah", 88)
t.__setitem__("Mya", 90)
t.__setitem__("Mar", 4)
t.__setitem__("precious", 10)
t.__setitem__("lady", 20)


print(t.arr, end ="\n")

print("\n",t["Ysenia"])
print(t["Xbox"])

print()
# print("After deleting xbix:")
# print(t.__delitem__("Xbox"))
# print()
# print(t.arr)