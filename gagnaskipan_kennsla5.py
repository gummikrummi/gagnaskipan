li = [1,2,3,4,5,6] 

def count_list(lst,count=0): 
    if not lst: 
        return count 
    else: 
        return count_list(lst[1:],count+1) 
    
print(count_list(li))