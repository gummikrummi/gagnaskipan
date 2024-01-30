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

def binary_search(arr,low,high,x):
#○ Implement binary search in an ordered list using recursive programming 
    if high >= low: 
        mid = (high + low) // 2 

        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x)  
    else: 
        return None 

my_arr = [2, 5, 7, 20, 100, 105, 207] 
x = 7 
res = binary_search(my_arr, 0, len(my_arr)-1, x)  
print(res)
print(my_arr[res]) 

def prefix(pre, a_str): 
    if not pre:
        return True 
    if not a_str or pre[0] != a_str[0]:
        return False 
    return prefix(pre[1:], a_str[1:])

def is_substring(substring, a_str):
#   ○ Implement the function is_substring(substring, a_str) that answers the
#     following:
#           ■ Is the string substring actually a substring in the list a_str?
#               ● Examples:
#                   ○ is_substring(“a”, “gagnaskipan”) -> True
#                   ○ is_substring(“gnask”, “gagnaskipan”) -> True
#                   ○ is_substring(“iganpsk”, “gagnaskipan”) -> False
#                   ○ is_substring(“gnAsk”, “gagnaskipan”) -> False
#                   ○ is_substring(“gnesk”, “gagnaskipan”) -> False
#           ■ Use recursion
#           ■ Hint: Try to first implement the function prefix(prefix, a_str)
#               ● Only checks whether prefix is an exact duplicate of the beginning
#                 of a_str
#           ■ There are two recursive/iterative “loops”.
#               ● Try to implement both loops with recursion
#                   ○ This solution can look elegant and clean! 
    if not substring:
        return True 
    if not a_str: 
        return False
    if prefix(substring, a_str):
        return True 
    return is_substring(substring, a_str[1:])
    
print(is_substring("a", "gagnaskipan")) 
print(is_substring("gnask", "gagnaskipan")) 
print(is_substring("iganpsk", "gagnaskipan")) 
print(is_substring("gnAsk", "gagnaskipan")) 
print(is_substring("gnesk", "gagnaskipan"))  

#Elfish / X-ish
#   ○ Implement the function x_ish(a_str, x) that answers the following:
#       ■ Does the string a_str include all letters in the string x?
#           ● Examples:
#               ○ x_ish(“gagnaskipan”, “a”) -> True
#               ○ x_ish(“gagnaskipan”, “gnask”) -> True
#               ○ x_ish(“gagnaskipan”, “iganpsk”) -> True
#               ○ x_ish(“gagnaskipan”, “gnAsk”) -> False
#               ○ x_ish(“gagnaskipan”, “gnesk”) -> False
#       ■ Use recursion
#       ■ Hint: Try to first implement the function elf_ish(a_str)
#           ● Only checks whether a_str includes all letters in the substring
#             “elf”
#       ■ There are two recursive/iterative “loops” and it affects the efficiency of the
#         solution which one is the “outer loop” and which one the “inner loop”.
#           ● Try to implement both loops with recursion
#               ○ This solution can look elegant and clean! 
def x_ish(a_str, x):
    if not x:
        return True 
    if not a_str: 
        return False
    if is_substring(x[0], a_str):
        return x_ish(a_str, x[1:])
    return False 
print(x_ish("gagnaskipan", "a")) 
print(x_ish("gagnaskipan", "gnask")) 
print(x_ish("gagnaskipan", "iganpsk")) 
print(x_ish("gagnaskipan", "gnAsk")) 
print(x_ish("gagnaskipan", "gnesk")) 
 
#Palindrome
#   ○ Implement the function palindrome that takes a string as a parameter:
#       ■ Returns True if the string reads exactly the same forwards and
#         backwards.
#       ■ Hint: You can make a helper function that takes different parameters
#           ● One possibility (of many) is a helper that takes two strings
#   ○ But send the same string into both parameters? 
def palindrome(a_str):
    if not a_str:
        return True 
    if a_str[0] == a_str[-1]:
        return palindrome(a_str[1:-1])
    return False 
print(palindrome("anna")) 
print(palindrome("annaa")) 
print(palindrome("annaaa"))




