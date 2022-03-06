#############################

# Heap Sort Practice

#############################


def heapify(array, number, i):
    """ Heapify a subtree rooted at a index i """
    
    largest = i # set for root
    left = 2 * i + 1 
    right = 2 * i+ 2 
    
    
    # see if left child root exists and is greater than root 
    if left < number and array[largest] < array[left]:
        largest = left 
    
    # see if right child root exists and is greater than root 

    if right < number and array[largest] < array[right]:
        largest = right 
        
    
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i] # swap 

    
        # heapify root 
        
        heapify(array,number,largest)
        
        
def heapSort(array):
    
    n = len(array)
    
    # build maxheap 
    
    for i in range(n//2 - 1 , -1, -1):
        heapify(array,n,i)
        
    # One by one extract elements 
    
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array,i,0)
        
        
#driver 

# Driver code
arr = [12, 11, 13, 5, 6, 7]
print("Array before heap sort: ")
for i in range(len(arr)):
    print(arr[i])
    
print() 

heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),
    

