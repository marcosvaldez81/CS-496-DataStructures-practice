################################################################################

# Marcos Valdez RED-ID: 821529898
# Professor Liu
# CS 496
# San Diego State University

################################################################################



# QUESTION 2

import random 
 
def my_matrix(n):
     
    """ this function is to generate a random 2D matrix, calculate mean value of all elements in matrix, 
        create a new matrix B as the transpose of A, and lastly subtract the mean value from each element of 
        B and return modified matrix B  """
         
    A = [] #initiate list A
     
    mean_A = 0
    try:
        for i in range(n): #row 
            my_row = [] #rows for 2D matrix
             
            for k in range(n): # in order to create a 2D array, need a nested for loop. So this for loop is the column
                my_row.append(random.randint(0,255))
                mean_A = mean_A + my_row[k]
            A.append(my_row)
         
        mean_A = mean_A / (n*n) #calculate the mean
        print("Mean value is: ", mean_A)    
        print()
    
    except:
        print("Sorry, there was an error finding the maximum element. Please ensure you are using numbers and not weird symbols/alphabet.")
    # Now do similar for the B matrix
    B = []    
     
    for i in range(n):
        new_row = []
         
        for k in range(n):
            new_row.append(A[k][i]) # using the transpose of A as hw asked
            new_row[k] = new_row[k] - mean_A #subtract the mean
        B.append(new_row)
        
        
    return B #return modified matrix --- ***SEE DOC FOR EXPLANATION OF RUN TIME****
        

print("OUTPUT FOR QUESTION 2:\nSee run time on HW#3 PDF. ")    

try: 
    test = int(input("Enter a number: ")) 
    mod_matrix = my_matrix(test)
    print("Modified Matrix:")
    for i in range(test):
        for k in range(test):
            # wanted a clean output, so rounded to 2 decimal places.
            print(str(round(mod_matrix[i][k],2)) ,end = ' ')
          
        print("")
    
    print()
except :
    print("Sorry, there was an error finding the maximum element. Please ensure you are using numbers and not weird symbols/alphabet.")

    print()

#----------------


# QUESTION 4


class _Node:
    
    def __init__(self, element):      # initialize node's fields      
        self._element = element               # reference to integers      
        self._next = None                   # reference to next node
    
    
class linked_List:
    def __init__(self):    
        """Create an empty list."""    
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements
    
    
    def push(self, element):
        """ To push items in linked list """
        if self._head == None: 
            self._head = _Node(element) # if the head of the list is empty, then we will push the head in with self._size + 1
            self._size = self._size + 1
        else:
            obj = _Node(element)
            list_head = self._head
            
            while(list_head._next != None):
                list_head = list_head._next
                
            list_head._next = obj
            self._size = self._size + 1
    
 
            
    def length_list(self):
        """ This function is to return size of linked list """
        
        return self._size
    
    def return_max(self):
        """ This function is to return the max of the linked list"""
        max = 0
        
        
        list_head = self._head
        
        while(list_head != None):
              
            if(list_head._element > max):
                max = list_head._element
         
         
            list_head = list_head._next 
        return max 
    

# Test the code below:
print("OUTPUT FOR QUESTION 4: ")
print("Here is a print out of items in a simple linked list.")
test_list1 = linked_List()
test_list1.push(10)
test_list1.push(5)
test_list1.push(9)

try:
    
    head = test_list1._head
    while (head != None):
        print(head._element)
        head = head._next
    print("")
    print("length of the sample linked list: ", test_list1.length_list())
    print("Maximum element of the sample linked list: ", test_list1.return_max())
        
except :
    print("Sorry, there was an error finding the maximum element. Please ensure you are using numbers and not weird symbols/alphabet.")

print("")

# ----------------


# Question 5

def merge_lists(list_1, list_2):
    """ This function is to merge two linked lists using the linked lists created in previous function """
    
    # holder for empty list
    list_holder = linked_List()
    
    # basically set the head of both linked lists
    head_list_1 = list_1._head 
    head_list_2 = list_2._head 
    
    while(head_list_1 != None and head_list_2 != None):
        
        if(head_list_1._element <= head_list_2._element):
            list_holder.push(head_list_1._element) # insert the smaller element to the holder 
            head_list_1 = head_list_1._next # next element in list (kinda like adding 1 to a while loop to keep iterating)
        
        else:
            list_holder.push(head_list_2._element) # insert the smaller element to the holder 
            head_list_2 = head_list_2._next # next element in list for list_2
    
    # Anything remaining in list 1 and 2 will be inserted to the list holder. Need this for error handling
            
    while(head_list_1 != None):
        list_holder.push(head_list_1._element)
        head_list_1 = head_list_1._next
    while(head_list_2 != None):
        list_holder.push(head_list_2._element)
        head_list_2 = head_list_2._next
        
        
    return list_holder


# Need to create a first and second linked list: 
test_list2 = linked_List()

test_list2.push(1)
test_list2.push(3)
test_list2.push(5)

 
# second linked list
test_list3 = linked_List()
test_list3.push(2)
test_list3.push(4)
test_list3.push(6)



# call the merge_lists function
my_merged_list = merge_lists(test_list2, test_list3)


# here I print the elements of the now merged list
print("QUESTION 5:")
print("Here is a print out of items in the now merged list using HW sample lists. Run time analysis is on the HW#3 PDF.")
try:
    head1 = my_merged_list._head
    while(head1 != None):
        print(head1._element)
        head1 = head1._next


except :
    print("Sorry, there was an error finding the maximum element. Please ensure you are using numbers and not weird symbols/alphabet.")

