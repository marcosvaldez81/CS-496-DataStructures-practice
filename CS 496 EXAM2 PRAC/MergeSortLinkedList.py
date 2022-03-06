#############################


# Merge Sort with Linked List Practice

#############################

# Merge sort with Linked List 



# first we need to create a Node using Class Node

class Node:
    
    def __init__(self,data):
        self.data = data 
        self.next = None 
        

class LinkedList:
    
    def __init__(self):
        self.head = None 
        
    
    # we need to push the new value to linked list using append
    
    def append(self,new_item):
        
        # Use Node Class
        new_node = Node(new_item) 
        
        # if the head is empty, put new Node there 
        
        if self.head is None:
            self.head = new_node 
            return 
        
        current_node = self.head
        
        while current_node.next is not None:
            current_node = current_node.next
        
        # append the new node at end 
        
        current_node.next = new_node


    def sortedMerge(self,a,b):
        
        result = None 
        
        # Base Case 
        
        if a == None:
            return b 
        
        if b == None:
            return a 
        
        # pick a or b and recur 
        
        if a.data <= b.data:
            result = a 
            result.next = self.sortedMerge(a.next,b)
            
        else:
            result = b 
            result.next = self.sortedMerge(a ,b.next)
            
        return result 
    
    def getMiddle(self,head):
        """ To get the middle of a linked list """
        if(head == None):
            return head 
        
        slow = head 
        fast = head 
        
        while(fast.next != None and fast.next.next != None):
            slow = slow.next 
            fast = fast.next.next 
            
        return slow 


   
    def mergeSort(self,head):
        
        if head == None or head.next == None:
            return head 
        
        # now we get the middle of the linked list 
        
        middle = self.getMiddle(head)
        next_middle = middle.next
        
        # set next of middle node to None
        middle.next = None 
        
        
        # apply mergesort to left list 
        
        left = self.mergeSort(head)
        
        right = self.mergeSort(next_middle)
        
        
        # Merge left and right lists 
        
        sorted_list = self.sortedMerge(left, right)
        
        return sorted_list
    
    

def printList(head):
    if head is None:
        print(' ')
        return 
    
    current_node = head 
    
    while current_node:
        print(current_node.data, end = ' ')
        current_node = current_node.next 
        
    print()
  
# Driver Code
if __name__ == '__main__':
    li = LinkedList()
     
    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)
    
    print("Linked list before merge sort: ")
    printList(li.head)
    print()
    # Apply merge Sort
    li.head = li.mergeSort(li.head)
    print ("Sorted Linked List is:")
    printList(li.head)
  
        


