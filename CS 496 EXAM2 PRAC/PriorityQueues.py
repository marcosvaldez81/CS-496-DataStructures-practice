#############################

# Priority Queues Practice

#############################



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
       
   
    
if __name__ == '__main__':
    queue = PriorityQueue()
    queue.insert(15)
    queue.insert(5)
    queue.insert(2)
    queue.insert(100)
    
    print(queue)
    
    while not(queue.isEmpty()):
        print(queue.delete())
