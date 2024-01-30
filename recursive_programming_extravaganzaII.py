def length_of_string(string):
    #○ Implement a recursive function that calculates the length of a string
    #○ Takes a string as a parameter
    #○ Returns an integer (+1 for each character)
#Note that you can use built in syntax for a string exactly as if it were a list where each
#item is a character. “abcd”[2] == ‘c’ ... “abcd”[:-1] == “abc” ... “abcd”[1:] == “bcd” 

    if not string:
        return 0
    else:
        return length_of_string(string[1:]) + 1  
print(length_of_string("Hello World!"))
    
def linear_search(lst, val): 

#   ○ Implement a recursive function that searches for a value in a list
#   ○ Takes a list and a single value as parameters
#   ○ Returns a boolean value
#       ■ True if the value is in the list, otherwise False 
    if not lst:
        return False 
    elif lst[0] == val: 
        return True 
    else: 
        return linear_search(lst[1:],val) 
print(linear_search([1,2,3,4,5,6,7,8,9], 10))
    
def count_instances(lst, val):
#   ○ Implement a recursive function that counts a specific value in a list
#   ○ Takes a list and a single value as parameters
#   ○ Returns an integer value
#       ■ How many times does that value appear in the list? 
    if not lst:
        return 0
    elif lst[0] == val:
        return count_instances(lst[1:],val) + 1
    else:
        return count_instances(lst[1:],val) 
print(count_instances([1,2,3,4,5,6,7,8,9], 9))

def are_there_duplicates_in_a_list(lst):
#   ○ Implement a recursive function that checks for duplicate values in a list
#   ○ Takes a list as a parameter
#   ○ Returns a boolean value
#       ■ True if any value in the list appears more than once, otherwise False 
    if not lst:
        return False
    elif lst[0] in lst[1:]:
        return True
    else:
        return are_there_duplicates_in_a_list(lst[1:]) 
print(are_there_duplicates_in_a_list([1,2,3,4,5,6,7,8,9]))  

def remove_duplicates(lst):
#   ○ Implement a recursive function that removes duplicate values in a list
#   ○ Takes a list as a parameter
#   ○ Returns another list
#       ■ List with all the same values, but only one instance of each value 
    if not lst:
        return []
    elif lst[0] in lst[1:]:
        return remove_duplicates(lst[1:])
    else:
        return [lst[0]] + remove_duplicates(lst[1:]) 
print(remove_duplicates([1,2,3,4,5,6,7,8,9,1,2,3]))