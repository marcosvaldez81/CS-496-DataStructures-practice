#############################
 
# QuickSort Youtube Practice
 
#############################

# average run time : O(nlogn)


def swap(a, b, arr):
    
    if a!=b:
        # this code block is the standard way across languages
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
    
    #arr[a], arr[b] = arr[b], arr[a] --> this way is the python easy way
    
    
    

def partition(elements,start,end):
    index = start
    pivot = elements[index]
    
    start = index + 1 
    
    end = len(elements) - 1
    
    while start < end:
        
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end = end - 1 
            
            
        if start<end:
             
            swap(start,end,elements)
    
    swap(index,end,elements)

    return end 

def quick_sort(elements,start,end):
    
    if start < end:
        part_index = partition(elements,start,end)
        
        quick_sort(elements,start,part_index -1) # left partition
        quick_sort(elements,part_index + 1, end) # right partition 
    
    
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements,0,len(elements)-1)
    print(elements)
    print()
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
    
    