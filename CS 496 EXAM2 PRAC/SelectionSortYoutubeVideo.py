#############################
 
# Selection Sort Youtube Practice
 
#############################


# find the smallest element in list then swap with first element

# O(n^2) complexity 



def find_min(arr):
    min = 1000000
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
             
    return min 


def selection_sort(arr):
    
    size = len(arr)
    for i in range(size -1):
        
        minimum_index = i # this first for loop is the very first i in the list/array (arr[0])
        
        for j in range(minimum_index + 1, size): # this for loop is needed to iterate from arr[1] +. 
            if arr[j] < arr[minimum_index]: # if the iterator is smaller than the minimum index (arr[0])...
                
                minimum_index = j # swap!
        
        if i != minimum_index:
        
            arr[i],arr[minimum_index] = arr[minimum_index], arr[i] # do the swap official

# driver 

if __name__ == '__main__':
    elements = [78 ,12, 15, 8 ,2, 61, 53, 23 , 27]
    selection_sort(elements)
    print(find_min(elements))
    print(elements)
    
