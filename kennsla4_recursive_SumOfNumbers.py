#sum of digits code recursive 
def sod(n): 
    if n == 0: #base case
        return 0 
    
    return (n % 10) + sod(n//10) #skilar summu af tölunum 
