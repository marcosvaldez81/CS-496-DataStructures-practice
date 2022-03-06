################################################################################

# Marcos Valdez RED-ID: 821529898
# Professor Liu
# CS 496
# San Diego State University

################################################################################



# Question 3

def non_recursion_1(number):
     
    """ This function will find the minimal number and maximal number in an unsorted sequence using non recursion. """
    
    low_holder = number[0]
    low = 0
    high = 0
     
    try:
        for num in number:
            # This if function handles any possible strings interpreted as ints
            if(num %2 ==0 and num %2 !=0):
                continue
                
            if num < low_holder:
                low = num
                 
            if num > low_holder:
                high = num
        
        return "High: "+ str(high) +"\n" +"Low: " + str(low) # run time O(n)
    
    except:
        return "Sorry, there was an error, please ensure you are inputting an integer and try again."

# mock_list1 = [10,2,5,100,8]
#  
# print(non_recursion_1(mock_list1))

 

def non_recursion2(numbers):
    """ This function is to find highest and lowest number in list using while loop  """
    
    
    try:
        
        for num in numbers:
            # This if function handles any possible strings interpreted as ints
            if(num %2 ==0 and num %2 !=0):
                continue
        holder = len(numbers)

        i = 0 
        high = numbers[0]
        low = numbers[0]
        while holder > i:
            
            if(numbers[i] < low):
                low = numbers[i]
                
            if(numbers[i] > high):
                high = numbers[i]

            i +=1
        
        return "High: " + str(high) +"\n"+ "Low: "+ str(low) # O(n)
    except:
        return "Sorry there was an error. Please ensure you are using list containing integers. "
    

# mock_list = [10,2,5,100,8]
#  
# print(non_recursion2(mock_list))





# Question 4
# --------------
def recursion_min(numbers, j):
    
    """ In this function I will find the high and low using recursion algorithm """
    
    try:
        for num in numbers:
            # This if function handles any possible strings interpreted as ints
            if(num %2 ==0 and num %2 !=0):
                continue
        if (j== 1):
            return numbers[0]
       
            
        return min(numbers[j- 1], recursion_min(numbers, j - 1)) # Run time O(n) 


            
    except:
        return "Error, please ensure you are using integers and not strings."




def recursion_high(numbers,j):
    
    """ This function will return lowest number of a list using recursion """
    try:
        for num in numbers:
            # This if function handles any possible strings interpreted as ints
            if(num %2 ==0 and num %2 !=0):
                continue
        if(j == 1):
            return(numbers[0])
        
        return max(numbers[j-1], recursion_high(numbers, j - 1)) # Run time O(n) or log(n)
    
    except:
        return "Error, please ensure you are using integers and not strings."
    

# list_1 = [5,66,87,9,1]
# j = len(list_1)
# print("Min:",recursion_min(list_1,j))
# print("High:",recursion_high(list_1,j))





# ---------------------

# Question 5

def reverse(user_input):
    
    """ This function will reverse the chars from an input using recursion  """
    #holder is good for error handling
    holder = str(user_input)
    if(len(holder) == 0):
        return holder
    
    
    # holder [1:0] is from index one, and we cut the holder[0] to append to the end.     
    return reverse(holder[1:]) + holder[0] # O(n)


# string = "SDSU@San"
# 
# print(reverse(string))
    
    




