#############################

# Selection Sort Practice

#############################


my_array = [66,25,12,22,11]

print("Unsorted array: ")
for i in range(len(my_array)):
    print(my_array[i])
    
    
for i in range(len(my_array)):
    min = i 
    
    for j in range(i+1, len(my_array)):
        if my_array[min] > my_array[j]:
            min = j 
            
    #Swap the minimum element w/ first element 
    my_array[i], my_array[min] = my_array[min], my_array[i]
    
print()
print("Sorted array: ")
for i in range(len(my_array)):
    print(my_array[i])

# Time complexity O(n^2) --> 2 nested loops
