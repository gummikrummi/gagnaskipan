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
    
def linear_search():
#   ○ Implement a recursive function that searches for a value in a list
#   ○ Takes a list and a single value as parameters
#   ○ Returns a boolean value
#       ■ True if the value is in the list, otherwise False 
    pass 

def count_instances():
#   ○ Implement a recursive function that counts a specific value in a list
#   ○ Takes a list and a single value as parameters
#   ○ Returns an integer value
#       ■ How many times does that value appear in the list? 
    pass 

def are_there_duplicates_in_a_list
#   ○ Implement a recursive function that checks for duplicate values in a list
#   ○ Takes a list as a parameter
#   ○ Returns a boolean value
#       ■ True if any value in the list appears more than once, otherwise False