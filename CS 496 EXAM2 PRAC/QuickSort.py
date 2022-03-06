#############################

# Quick Sort Practice

#############################


# Divide and Conquer algo 

# Key process is partition(), essentially use that as a pivot and move all items smaller than that pivot to the left of it, greater on the right


# This Function handles sorting part of quick sort start and end points to first and last element of an array respectively




def partition(start,end,arr):
    
    # initiate pivot index  to begin 
    index = start 
    pivot = arr[index]
    
    # This loop runs till start pointer crosses end pointer, and when it does we swap the pivot with element on end pointer

    while start < end:
        
        # Increment the start pointer till it finds an element greater than  pivot
        while start < len(arr) and arr[start] <= pivot:
            start+=1
            
        # Decrement the end pointer till it finds an element less than pivot
        while arr[end] > pivot:
            end -= 1
            
        # If start and end have not crossed each other, swap the numbers on start and end
        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]

    
    # Swap pivot element with element on end pointer This puts pivot on its correct sorted place.
    
    arr[end], arr[index] = arr[index], arr[end]
     
    # Returning end pointer to divide the array into 2
    return end


# Quick sort function:

def quick_sort(start,end, arr):
    
    if start < end :
         
        # p = partition for partitioning index, arr[p] us at right place 
        
        p = partition(start, end, arr)
        
        # sort element before partition & after partition 
        
        quick_sort(start, p -1, arr)
        
        quick_sort(p+1, end, arr)
        
        
        

#Driver 

array = [10,7,8,9,1,5]

print("array before sorting: ", array)
print()
quick_sort(0, len(array)-1, array) # worst case O(n^2)
        
print("Sorted Array: ", array)


