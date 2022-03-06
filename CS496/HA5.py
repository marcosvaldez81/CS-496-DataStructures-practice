############################################################


# Marcos Valdez
# CS 496 Data Structures 


############################################################



# Question 3) 

def partition(starter,end_list,my_array):
     
    """ Partition function needed for quick sort algo function below. Need a partitioner for iterating the quick sort. """
    # need a pivot index to begin partition process 
    index = starter 
    pivot = my_array[index]
    
    # while loop will run till the start pointer = end pointer
    while starter < end_list:

        while starter < len(my_array) and my_array[starter] <= pivot:
            starter+=1
             
        while my_array[end_list] > pivot:
            end_list -= 1
             
        if(starter < end_list):
            my_array[starter], my_array[end_list] = my_array[end_list], my_array[starter]
 
    # Swap pivot with end 
    my_array[end_list], my_array[index] = my_array[index], my_array[end_list]
      
    return end_list
 
 

# Quick sort function:
 
def quick_sort(starter,end_list, my_array):
    """ Quick Sort Algorithm relying on partition function to correctly partake in quicksort theorem """
    
    if starter < end_list :
          
        # partition_holder is needed to partition the index 
         
        partition_holder = partition(starter, end_list, my_array)
         
        # sort element before partition & after partition 
         
        quick_sort(starter, partition_holder -1, my_array) #quick sort end of list
         
        quick_sort(partition_holder+1, end_list, my_array) # quick sort start of list



# This function is the with the S sequence (HW FUNCTION REQUIREMENT)
def winner(S):
    """ Essentially will return last element of list with most votes """
    
    winner = S[-1] # after quick sort, the last element of list is answer!
    
    return winner


# Test it !
S=[10, 874, 10, 874, 92, 384, 92, 874]

quick_sort(0, len(S) -1 , S) # 0 = start, len(S) -1 = end , S is the list sequence

print("List after running quick sort function/algorithm:") # First lets print the now sorted list
print(S)
print("\nWinner is: ",winner(S)) # print the winner! (874!)

