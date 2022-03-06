############################################################


# Marcos Valdez
# CS 496 Data Structures 


############################################################



# Question 1:

def factorial_of_number(num):
    """ My function essentially will calculate the factorial of a number."""
    
    output = "null"
    try:
        if int(num) > 0:
            return num * factorial_of_number(num - 1)
           
    
        elif num == 0:
            return 1
        
        else:
            return output
        
    except:
        return "Sorry, there was an error. Ensure you are inputting a positive integer."

# print(factorial_of_number(5))
# print(factorial_of_number(0))
# print(factorial_of_number("abc"))  #--> would print correct output



# -----------------------------



# Question 2:

def sequence(number):
    """ This function will see if there is a distinct pair of numbers in the sequence, if there is an odd """
    
    try:
        first_number = number[0]
         
        for item in range(1,len(number)):
            if first_number * number[item] %2 != 0:
                return True
                break
            else:
                return False
    except:
        return "Sorry, there was an error. Please ensure the inputted code is in list form. For instance, sequence[1,3,5]"

# print(sequence([2,4,5]))# --> must be a list -- False
# print(sequence([1,3,4])) # True

# -------------------------



# Question 3:
 
def split(number):
     
    """ This definition will flip the inputted number. """
    try:
        if number > 0:
            # convert to string
            #[::-1] basically means -> start:stop:step 
            #Hence -1 starts at the end of the number and not the front. 
            return (str(number)[::-1])
         
        else:
            #first rotate
            rotate = (str(number)[::-1])
             
            #this final_rotate gets rid of the last number. hence [:-1] means the stop is the last number (-1) and it removes it.
            final_rotate = str(rotate[:-1]  )
       
            return "-" + final_rotate
    except:
        return "Error, please ensure you are inputting a integer."
    
    
#print(split(-1245))    
         
         
# -------------------------    
 


# Question 4:


def remove_string(word):
      
    """ This function will remove all commas in the inputted string. """
 
    try:  
        word.replace(',',' ')
        for character in word:
            if character == ",":
                word_holder = word.replace(',','')
                return word_holder
                  
            else:
                continue
    except:
        return "Sorry, there was an error. Ensure the input item is a string and not a integer/float."
        
        
#print(remove_string("Sit down, please"))


# -------------------------    

 
# Question 5
  
def valid(sentence):
     
    """ Checks if the string is valid based on parameters in assignment task.  """


    try:
        
        #first create special lists 
        special_list1 = ['(', '{', '[']
        special_list2 = [')', '}', ']']

        # new stack
        my_stack = []
        
        # this holder list is to collect non special chars stated in the assignment
        holder_list = []
        
        for item in sentence:
            
            if item not in special_list1:
                if item not in special_list2:
                    holder_list.append(item)
                    
            if item in special_list1:
                my_stack.append(item)
             
            if item in special_list2:
                
                # hold the item to close the special char
                holder = special_list2.index(item)
                
                if len(my_stack) > 0 and special_list1[holder] == my_stack[len(my_stack) - 1]:
                    #pop the stack, essentially pops off the top of the stack
                    my_stack.pop()
                     
                else:
                    return "False"
                

        if len(my_stack) == 0 and len(holder_list) == 0:
            return True
        else:
            return False 
    except:
        return "Error, ensure you are inputting the special chars from HW assignment."
       
# print(valid("[()]")) -- True
# print(valid("Hello world")) --> False
#print(valid(123)) --> False 


# -------------------------  


# Question 6

def merge_sort(first_list, second_list):
    """ This function is to combine both lists and put them in order. """
    
    try:
        
        #extend the first list so that second list can be appended
        first_list.extend(second_list)
        #sort the list
        first_list.sort()
         
        return first_list
    except:
        return "Sorry, there was an error."


#print(merge_sort([1,3,4], [1,2,6,8]))
 
 
 




    
