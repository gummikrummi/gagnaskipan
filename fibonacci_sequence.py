#fibonacci sequence 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    elif n < 0: 
        return "Invalid input, please enter a positive integer"
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 
    
print(fibonacci(8))  #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...