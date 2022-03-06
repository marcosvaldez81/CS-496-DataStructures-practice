#############################

# Merge Sort Practice

#############################


# Python function for implementing MergeSort with an Array

def mergeSort(arr):
    if len(arr)>1:
       
        #find middle of array
        middle = len(arr)//2
       
        #divide array of elements
        left = arr[:middle]
       
        #right half
        right = arr[middle:]
       
        #sort first half
        mergeSort(left)
       
        # sort second half
        mergeSort(right)
       
        i = j = k = 0 # all vars = 0
       
        #copy the data to temp arrays L[] and R[]
       
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]= left[i]
                i +=1
            else:
                arr[k] = right[j]
                j +=1
            k +=1
           
        # this code block is to check if any element is left
        while i < len(left):
            arr[k] = left[i]
            i +=1
            k +=1
           
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# code block is to print the  list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
       
    print()
   
# if __name__ == '__main__':
#     arr = [12,11,13,5,6,7]
#     print("OG array: ")
#     printList(arr)
#     print()
#     print("Now merge sorting...")
#     print()
#     mergeSort(arr)
#     print("Sorted array is: ", end = "\n")
#     printList(arr)

# ------------------------

# Merge sort with an Linked List